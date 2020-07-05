# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread(r'pictures\star.jpg', 0)
img2 = cv2.imread(r'pictures\star2.jpg', 0)
img3 = cv2.imread(r'pictures\rectangle1.jpg', 0)

ret, thresh = cv2.threshold(img1, 127, 255, 0)
ret, thresh2 = cv2.threshold(img2, 127, 255, 0)
ret, thresh3 = cv2.threshold(img3, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 2, 1)
cnt1 = contours[0]
contours, hierarchy = cv2.findContours(thresh2, 2, 1)
cnt2 = contours[0]
contours, hierarchy = cv2.findContours(thresh3, 2, 1)
cnt3 = contours[0]

ret0 = cv2.matchShapes(cnt1, cnt1, 1, 0.0)
ret1 = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
ret2 = cv2.matchShapes(cnt1, cnt3, 1, 0.0)
print(ret0, ret1, ret2)
