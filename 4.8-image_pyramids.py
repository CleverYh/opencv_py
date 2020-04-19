# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'pictures\a.05x.jpg')
higher_reso = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
lower_reso = cv2.pyrDown(higher_reso)
higher_reso2 = cv2.pyrUp(lower_reso)

# Normally, we used to work with an image of constant size. But in some occassions, we need to work with images of different resolution of the same image. For example, while searching for something in an image, like face, we are not sure at what size the object will be present in the image. In that case, we will need to create a set of images with different resolution and search for object in all the images. These set of images with different resolution are called Image Pyramids (because when they are kept in a stack with biggest image at bottom and smallest image at top look like a pyramid).
# There are two kinds of Image Pyramids. 1) Gaussian Pyramid and 2) Laplacian Pyramids
# Higher level (Low resolution) in a Gaussian Pyramid is formed by removing consecutive rows and columns in Lower level (higher resolution) image. Then each pixel in higher level is formed by the contribution from 5 pixels in underlying level with gaussian weights. By doing so, a M \times N image becomes M/2 \times N/2 image. So area reduces to one-fourth of original area. It is called an Octave. The same pattern continues as we go upper in pyramid (ie, resolution decreases). Similarly while expanding, area becomes 4 times in each level. We can find Gaussian pyramids using cv2.pyrDown() and cv2.pyrUp() functions.
# Laplacian Pyramids are formed from the Gaussian Pyramids. There is no exclusive function for that. Laplacian pyramid images are like edge images only. Most of its elements are zeros. They are used in image compression. A level in Laplacian Pyramid is formed by the difference between that level in Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid.

plt.subplot(2, 2, 1), plt.imshow(higher_reso, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(lower_reso, cmap='gray')
plt.title('lower_reso'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(higher_reso2, cmap='gray')
plt.title('higher_reso2'), plt.xticks([]), plt.yticks([])

plt.show()
