# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

# Histogram backprojection was proposed by Michael J. Swain , Dana H. Ballard in their paper Indexing via color histograms.

# What is it actually in simple words? It is used for image segmentation or finding objects of interest in an image. In simple words, it creates an image of the same size (but single channel) as that of our input image, where each pixel corresponds to the probability of that pixel belonging to our object. In more simpler worlds, the output image will have our object of interest in more white compared to remaining part. Well, that is an intuitive explanation. (I can’t make it more simpler). Histogram Backprojection is used with camshift algorithm etc.

# How do we do it ? We create a histogram of an image containing our object of interest (in our case, the ground, leaving player and other things). The object should fill the image as far as possible for better results. And a color histogram is preferred over grayscale histogram, because color of the object is more better way to define the object than its grayscale intensity. We then “back-project” this histogram over our test image where we need to find the object, ie in other words, we calculate the probability of every pixel belonging to the ground and show it. The resulting output on proper thresholding gives us the ground alone.

# In numpy
# 1. First we need to calculate the color histogram of both the object we need to find (let it be ‘M’) and the image where we are going to search (let it be ‘I’).
# roi is the object or region of object we need to find
roi = cv2.imread(r'pictures\roi.a.2x.jpg')
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)

# target is the image we search in
target = cv2.imread(r'pictures\a.2x.jpg')
hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
target_rgb = cv2.cvtColor(target, cv2.COLOR_BGR2RGB)

# Find the histograms using calcHist. Can be done with np.histogram2d also
M = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
I = cv2.calcHist([hsvt], [0, 1], None, [180, 256], [0, 180, 0, 256])

# 2. Find the ratio R = \frac{M}{I}. Then backproject R, ie use R as palette and create a new image with every pixel as its corresponding probability of being target. ie B(x,y) = R[h(x,y),s(x,y)] where h is hue and s is saturation of the pixel at (x,y). After that apply the condition B(x,y) = min[B(x,y), 1].

# I[I == 0] = 0.01 # invalid value encountered in true_divide
R = M/I # R = np.divide(M,I)

h, s, v = cv2.split(hsvt)
B = R[h.ravel(), s.ravel()]
B = np.minimum(B, 1)
B = B.reshape(hsvt.shape[:2])

# 3. Now apply a convolution with a circular disc, B = D \ast B, where D is the disc kernel.

disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
cv2.filter2D(B, -1, disc, B)
B = np.uint8(B)
cv2.normalize(B, B, 0, 255, cv2.NORM_MINMAX)

# 4. Now the location of maximum intensity gives us the location of object. If we are expecting a region in the image, thresholding for a suitable value gives a nice result.

ret, thresh = cv2.threshold(B, 20, 255, 0)
thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2RGB)
res = cv2.bitwise_and(target_rgb,thresh)

plt.subplot(311), plt.imshow(roi_rgb)
plt.subplot(312), plt.imshow(target_rgb)
plt.subplot(313), plt.imshow(res)

plt.show()
