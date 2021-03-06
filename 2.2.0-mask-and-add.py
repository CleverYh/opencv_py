# coding: utf-8
from cv2 import cv2
import numpy as np

img_1 = cv2.imread(r'pictures\a.jpg')
img_2 = cv2.imread(r'pictures\save.jpg')

# There is a difference between OpenCV addition and Numpy addition. OpenCV addition is a saturated operation while Numpy addition is a modulo operation.
# >>> y = np.uint8([10])
# >>> print cv2.add(x,y) # 250+10 = 260 => 255
# [[255]]
# >>> print x+y          # 250+10 = 260 % 256 = 4
# [4]
# It will be more visible when you add two images. OpenCV function will provide a better result. So always better stick to OpenCV functions.

img_numpy_add = img_1 + img_2

roi_img = np.zeros(img_2.shape[0:2], dtype=np.uint8)
print(img_2.shape[0:2])  # (1653, 2339)
roi_img[100:1000, 300:1600] = 255

img_add = cv2.add(img_2, img_2)
img_add_mask = cv2.add(img_2, img_2, mask=roi_img)
cv2.namedWindow("img_add", 0)
cv2.imshow("img_add", img_add)
cv2.namedWindow("img_numpy_add", 0)
cv2.imshow("img_numpy_add", img_numpy_add)
cv2.waitKey(0)
cv2.namedWindow("img_add_mask", 0)
cv2.imshow("img_add_mask", img_add_mask)
cv2.waitKey(0)

cv2.destroyAllWindows()

# src1, alpha, src2, beta, gamma(最后加上常量值) 图片大小通道应该相同。
blend = cv2.addWeighted(img_1, 0.4, img_2, 0.6, 0)

cv2.namedWindow("blend", 0)
cv2.imshow("blend", blend)
cv2.waitKey(0)
cv2.destroyAllWindows()
