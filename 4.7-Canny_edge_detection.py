# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'pictures\souji.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
edges = cv2.Canny(img, 100, 200)
# def Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None) # The smallest value between threshold1 and threshold2 is used for edge linking. The . largest value is used to find initial segments of strong edges.

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

# Canny Edge Detection is a popular edge detection algorithm. It was developed by John F. Canny in 1986. It is a multi-stage algorithm.
# 1.Noise Reduction: Since edge detection is susceptible to noise in the image, first step is to remove the noise in the image with a 5x5 Gaussian filter. 
# Finding Intensity Gradient of the Image: Smoothened image is then filtered with a Sobel kernel in both horizontal and vertical direction to get first derivative in horizontal direction (G_x) and vertical direction (G_y). From these two images, we can find edge gradient and direction for each pixel as follows: $Edge\_Gradient \; (G) = \sqrt{G_x^2 + G_y^2}$  $Angle \; (\theta) = \tan^{-1} \bigg(\frac{G_y}{G_x}\bigg)$ Gradient direction is always perpendicular to edges. It is rounded to one of four angles representing vertical, horizontal and two diagonal directions.
# Non-maximum Suppression: After getting gradient magnitude and direction, a full scan of image is done to remove any unwanted pixels which may not constitute the edge. For this, at every pixel, pixel is checked if it is a local maximum in its neighborhood in the direction of gradient.
# Hysteresis Thresholding：This stage decides which are all edges are really edges and which are not. For this, we need two threshold values, minVal and maxVal. Any edges with intensity gradient more than maxVal are sure to be edges and those below minVal are sure to be non-edges, so discarded. Those who lie between these two thresholds are classified edges or non-edges based on their connectivity. If they are connected to “sure-edge” pixels, they are considered to be part of edges. Otherwise, they are also discarded. This stage also removes small pixels noises on the assumption that edges are long lines. So what we finally get is strong edges in the image.
# OpenCV puts all the above in single function, cv2.Canny().