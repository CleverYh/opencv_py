# coding: utf-8
from cv2 import cv2
import numpy as np

cv2.namedWindow("Video", cv2.WINDOW_AUTOSIZE)
cap = cv2.VideoCapture(r'pictures\video.mov')

while (cap.isOpened()):
    ret, frame = cap.read()  # ret return bool

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
