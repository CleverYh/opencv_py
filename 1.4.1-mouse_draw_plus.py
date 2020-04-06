# coding: utf-8
from cv2 import cv2
import numpy as np

###### 默认画矩形, 按M改变模式, 可以画直线 ######
###### 但是鼠标速度不宜过快 #################### 

drawing = False  # true if mouse is pressed
mode = True  # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1

# mouse callback function

def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (255, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 5, (255, 128, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img, (ix, iy), (x, y), (255, 255, 0), -1)
        else:
            cv2.circle(img, (x, y), 5, (225, 128, 255), -1)

img = np.ones((1024, 1024, 3), np.uint8)
img = 255*img

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()
