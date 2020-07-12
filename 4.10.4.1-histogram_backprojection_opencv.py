# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

# OpenCV provides an built-in function cv2.calcBackProject(). Its parameters are almost same as the cv2.calcHist() function. One of its parameter is histogram which is histogram of the object and we have to find it. Also, the object histogram should be normalized before passing on to the backproject function. It returns the probability image. Then we convolve the image with a disc kernel and apply threshold.

roi = cv2.imread(r'pictures\roi.a.2x.jpg')
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

target = cv2.imread(r'pictures\a.2x.jpg')
hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
target_rgb = cv2.cvtColor(target, cv2.COLOR_BGR2RGB)

# calculating object histogram
roihist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

# normalize histogram and apply backprojection
cv2.normalize(roihist, roihist, 0, 255, cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)

# Now convolute with circular disc
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
cv2.filter2D(dst, -1, disc, dst)

# threshold and binary AND
ret, thresh = cv2.threshold(dst, 50, 255, 0)
thresh = cv2.merge((thresh, thresh, thresh))
res = cv2.bitwise_and(target_rgb, thresh)

# res = np.vstack((target,thresh,res))
# cv2.imwrite('res.jpg',res)
plt.subplot(311), plt.imshow(target_rgb)
plt.subplot(312), plt.imshow(thresh)
plt.subplot(313), plt.imshow(res)

plt.show()
