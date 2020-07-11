# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

# Consider an image whose pixel values are confined to some specific range of values only. For eg, brighter image will have all pixels confined to high values. But a good image will have pixels from all regions of the image. So you need to stretch this histogram to either ends and that is what Histogram Equalization does (in simple words). This normally improves the contrast of the image.

img = cv2.imread(r'pictures\equalization_opencv.jpg',0)

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

# You can see histogram lies in brighter region. We need the full spectrum. For that, we need a transformation function which maps the input pixels in brighter region to output pixels in full region. That is what histogram equalization does.
# Now we find the minimum histogram value (excluding 0) and apply the histogram equalization equation as given in wiki page. But I have used here, the masked array concept array from Numpy. For masked array, all operations are performed on non-masked elements. You can read more about it from Numpy docs on masked arrays.
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')

img2 = cdf[img]
# Now calculate its histogram and cdf as before
hist2,bins = np.histogram(img2.flatten(),256,[0,256])

cdf2 = hist2.cumsum()
cdf_normalized2 = cdf2 * hist2.max()/ cdf2.max()

plt.subplot(221),plt.imshow(img, 'gray')
plt.subplot(222),plt.plot(cdf_normalized, color = 'b'),plt.hist(img.flatten(),256,[0,256], color = 'r'),plt.xlim([0,256]),plt.legend(('cdf','histogram'), loc = 'upper left')
plt.subplot(223),plt.imshow(img2, 'gray')
plt.subplot(224),plt.plot(cdf_normalized2, color = 'b'),plt.hist(img2.flatten(),256,[0,256], color = 'r'),plt.xlim([0,256]),plt.legend(('cdf','histogram'), loc = 'upper left')

plt.show()

# Another important feature is that, even if the image was a darker image (instead of a brighter one we used), after equalization we will get almost the same image as we got. As a result, this is used as a “reference tool” to make all images with same lighting conditions. This is useful in many cases. For example, in face recognition, before training the face data, the images of faces are histogram equalized to make them all with same lighting conditions.

# About numpy.ma : https://blog.csdn.net/wzy628810/article/details/103833856
# Numpy Doc : https://docs.scipy.org/doc/numpy-1.13.0/reference/maskedarray.generic.html#maskedarray-generic-constructing