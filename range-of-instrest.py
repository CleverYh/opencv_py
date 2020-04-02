# coding: utf-8
from cv2 import cv2
import numpy as np

img = cv2.imread('a.jpg')
cv2.namedWindow("Demo")

roi = img[600:1200, 2100:3600]  # 1500x600 (r=600,c=1500)
cv2.imshow("Demo", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.namedWindow("Demo",0)
cv2.imshow("Demo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
img[0:600, 1000:2500] = roi
# b= img[:,:,0] # 截取蓝色通道
cv2.namedWindow("Demo",0)
cv2.imshow("Demo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()