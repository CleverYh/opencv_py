# coding: utf-8
from cv2 import cv2


ID = 0
print("Finding camera ID, please wait...")

while(1):
    cap = cv2.VideoCapture(ID)
    # get a frame
    ret, frame = cap.read()
    if ret == False:
        ID += 1
    else:
        print(ID)
        break

# throught this code, you can find your camera ID.