# coding: utf-8
from cv2 import cv2
import numpy as np

img = cv2.imread(r'pictures\lena.jpg')


def nothing(args):
    pass


img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.namedWindow('tracks', cv2.WINDOW_GUI_EXPANDED)

# cv2.createTrackbar() 为窗口添加trackbar
#     参数：
#         value: trackbar创建时的值
#         count：trackbar能设置的最大值，最小值总为0
#         onChange：trackbar值发生变化时的回调函数，trackbar的值作为参数传给onchange

#     cv2.getTrackbarPos() 获取某个窗口中trackbar的值

cv2.createTrackbar("LH", "tracks", 0, 255, nothing)
cv2.createTrackbar("LS", "tracks", 0, 255, nothing)
cv2.createTrackbar("LV", "tracks", 0, 255, nothing)

cv2.createTrackbar("UH", "tracks", 255, 255, nothing)
cv2.createTrackbar("US", "tracks", 255, 255, nothing)
cv2.createTrackbar("UV", "tracks", 255, 255, nothing)

# create switch for ON/OFF functionality
switch = "0:OFF \n1:ON"
cv2.createTrackbar(switch, "tracks", 0, 1, nothing)

while(1):

    # get current positions of four trackbars
    l_h = cv2.getTrackbarPos("LH", "tracks")
    l_s = cv2.getTrackbarPos("LS", "tracks")
    l_v = cv2.getTrackbarPos("LV", "tracks")
    u_h = cv2.getTrackbarPos("UH", "tracks")
    u_s = cv2.getTrackbarPos("US", "tracks")
    u_v = cv2.getTrackbarPos("UV", "tracks")
    s = cv2.getTrackbarPos(switch, "tracks")

    lower_b = np.array([l_h, l_s, l_v])
    upper_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(img_hsv, lower_b, upper_b)
    res = cv2.add(img, img, mask=mask)

    cv2.imshow("img", img)

    if s == 0:
        cv2.destroyWindow("mask")
        cv2.destroyWindow("res")
    else:
        cv2.imshow("mask", mask)
        cv2.imshow("res", res)

    k = cv2.waitKey(1)
    if k == ord("s") & s == 1:
        cv2.imwrite('1.5_temp_save_mask', mask)
        cv2.imwrite('1.5_temp_save_res', res)
        print("lower=", lower_b, "upper=", upper_b)
    elif k == 27:  # ESC to quit
        if s == 1:
            print("lower=", lower_b, "upper=", upper_b)
        break

cv2.destroyAllWindows()
