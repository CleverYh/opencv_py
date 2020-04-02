# coding: utf-8
from cv2 import cv2
import numpy as np
import imutils

img = cv2.imread('a.jpg')
reversed_img = 255 - img  # 对图像取反
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# init
random_img = np.zeros((gray_img.shape[0], gray_img.shape[1]), dtype=np.uint8)
# 线性变化(电脑很卡)(255溢出后会变黑)
# for i in range(gray_img.shape[0]):
#     for j in range(gray_img.shape[1]):
#         random_img[i, j] = gray_img[i, j]*1.5


cv2.imwrite(r"C:\Users\cortex\Documents\code\opencv_py\save.jpg", gray_img)
cv2.namedWindow("random_img", 0)
cv2.namedWindow("Reversed", 0)
cv2.imshow('Reversed', reversed_img)
# cv2.imshow('random_img', random_img)
cv2.imshow('random_img', gray_img)
# cv2.imshow('random_img', hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()