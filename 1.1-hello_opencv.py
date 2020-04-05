# coding: utf-8
from cv2 import cv2  # is equal to: import cv2
# because the latest opencv has cv2 in cv2, this way can prevent vscode reporting errors which makes me very annoyed
import numpy as np
import imutils

img = cv2.imread(r'pictures\a.jpg')
# img_gray = cv2.imread('pictures\a.jpg', 0)
# cv2.namedWindow("Example_1", cv2.WINDOW_AUTOSIZE) # 图片不缩放 窗口缩放
# 图片缩放以适应窗口
# cv2.namedWindow("Example_1", 0)
# cv2.imshow('Example_1', imutils.resize(img_gray, 1000))  # 横向像素长度
cv2.namedWindow("Example_2", 0)
cv2.imshow('Example_2', img)
cv2.waitKey(1000)
cv2.destroyAllWindows()