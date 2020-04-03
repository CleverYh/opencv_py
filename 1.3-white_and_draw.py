# coding: utf-8
from cv2 import cv2
import numpy as np

white_img = np.ones((512, 512, 3), np.uint8)  # init to [1, 1, 1]
white_img = 255*white_img  # [255, 255, 255]
cv2.imshow('white_img', white_img)
cv2.waitKey(1000)
cv2.destroyAllWindows()

# img： 表示需要进行绘制的图像对象ndarray
# color： 表示绘制几何图形的颜色，采用BGR即上述说的(B、G、R)
# thickness： 表示绘制几何图形中线的粗细，默认为1, 对于圆、椭圆等封闭图像取-1时是填充图形内部
# lineType ： 表示绘制几何图形线的类型，默认8-connected线是光滑的，当取cv2.LINE_AA时线呈现锯齿状
img = np.ones((512, 512, 3), np.uint8)
img = 255*img
img = cv2.line(img, (100, 100), (400, 400), (255, 0, 0), 5)
img = cv2.rectangle(img, (200, 20), (400, 120), (0, 255, 0), 3)
img = cv2.circle(img, (100, 400), 50, (0, 0, 255), 2)
img = cv2.circle(img, (250, 400), 50, (0, 0, 255), 0, cv2.LINE_AA)
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (0, 255, 255), -1)
pts = np.array([[100, 50], [200, 300], [70, 200], [50, 100]], np.int32)
img = cv2.polylines(img, [pts], True, (0, 0, 0), 2)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,250), font, 4,(255,255,0),2,cv2.LINE_AA)

cv2.imshow('img', img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
