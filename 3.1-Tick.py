# coding: utf-8
from cv2 import cv2
import numpy as np

###### 通过末时钟计数减去初时钟计数的差除以时钟频率计算时间 ######

img_1 = cv2.imread(r'pictures\lena.jpg')

e1 = cv2.getTickCount()
for i in range(7, 24, 2):
    img_1 = cv2.medianBlur(img_1, i)
e2 = cv2.getTickCount()

cv2.namedWindow("medianBlur")
cv2.imshow('medianBlur', img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

t = (e2 - e1)/cv2.getTickFrequency()
print('Process time: ',t, 's', sep='')