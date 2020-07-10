# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

# We used cv2.calcHist() to find the histogram of the full image. What if you want to find histograms of some regions of an image? Just create a mask image with white color on the region you want to find histogram and black otherwise. Then pass this as the mask.

img = cv2.imread(r'pictures\a.2x.jpg',0)

# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[200:400, 0:180] = 255
masked_img = cv2.bitwise_and(img,img,mask = mask)

# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()

# In the histogram plot, one upper line shows histogram of full image while another line which always below the upper line shows histogram of masked region.
