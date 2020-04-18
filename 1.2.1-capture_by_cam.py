# coding: utf-8
from cv2 import cv2
import numpy as np

cap = cv2.VideoCapture(700) # my cam ID is 700 on my notebook but it may not work on your computer. You can try to run "1.2.1.1-find-cam-id.py" to find your camera ID first.

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()