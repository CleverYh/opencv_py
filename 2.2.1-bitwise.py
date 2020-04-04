# coding: utf-8
from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt

img_1 = cv2.imread(r'pictures\opencv.png')
rows, cols = img_1.shape[0:2]
img_2 = cv2.imread(r'pictures\cat.jpg')
roi = img_2[0:rows, 0:cols]
img_1_gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)

ret, img_1_thres = cv2.threshold(img_1_gray, 200, 255, cv2.THRESH_BINARY_INV)
img_1_frontground = cv2.add(img_1, img_1, mask=img_1_thres)

print(img_1.shape, roi.shape)

img_1_thres_inv = cv2.bitwise_not(img_1_thres)  # 取反
roi_background = cv2.add(roi, roi, mask=img_1_thres_inv)

img_add = cv2.addWeighted(img_1_frontground, 0.6, roi_background, 1, 0)
img_2[0:rows, 0:cols] = img_add

cv2.imshow("gray", img_1_gray)
cv2.imshow("thres", img_1_thres)
cv2.imshow("fg", img_1_frontground)
cv2.imshow("tinv", img_1_thres_inv)
cv2.imshow("roi_bg", roi_background)
cv2.imshow("img_add", img_add)
cv2.imshow("img_2", img_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
