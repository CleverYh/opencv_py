# coding: utf-8
from cv2 import cv2
import numpy as np

black_img = np.ones((512, 512, 3), np.uint8)
white_img = 255*black_img


# 上－外圆－红色填充
black_img = cv2.circle(black_img, (256, 176), 40, (0, 0, 255), -1)
# 上－内圆－黑色填充
black_img = cv2.circle(black_img, (256, 176), 16, (0, 0, 0), -1)
 
# 左下－外圆－绿色填充
black_img = cv2.circle(black_img, (210, 256), 40, (0, 255, 0), -1)
# 左下－内圆－黑色填充
black_img = cv2.circle(black_img, (210, 256), 16, (0, 0, 0), -1)
 
# 右下－外圆－蓝色填充
black_img = cv2.circle(black_img, (302, 256), 40, (255, 0, 0), -1)
# 右下－内圆－黑色填充
black_img = cv2.circle(black_img, (302, 256), 16, (0, 0, 0), -1)
 
 
# 用一个四角的多边形来填充覆盖
pts = np.array([[256, 176], [210, 256], [250, 256], [276, 210]], np.int32)
pts = pts.reshape((-1, 1, 2))
black_img = cv2.fillPoly(black_img, [pts], (0, 0, 0))
 
# 第2个覆盖，使用三角形
pts2 = np.array([[276, 210], [302, 256], [322, 210]], np.int32)
pts2 = pts2.reshape((-1, 1, 2))
black_img = cv2.fillPoly(black_img, [pts2], (0, 0, 0))

# OpenCV
font = cv2.FONT_HERSHEY_SIMPLEX
black_img = cv2.putText(black_img,'OpenCV',(140,355), font, 2,(255,255,200),4,cv2.LINE_AA)

# white_img = 255-black_img
lower_red = np.array([1, 1, 1])
upper_red = np.array([255, 255, 255])
# mask -> 1 channel
white_img = cv2.inRange(black_img, lower_red, upper_red,(255,255,255))
 
cv2.imshow('draw exercise', black_img)

cv2.imshow("white",white_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
