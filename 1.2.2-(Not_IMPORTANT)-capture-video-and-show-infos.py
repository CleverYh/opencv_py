# coding: utf-8
from cv2 import cv2
import numpy as np

# capture = cv2.VideoCapture("./test.avi")
capture = cv2.VideoCapture(700)
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv2.CAP_PROP_FPS)
print(height, width, count, fps)
out = cv2.VideoWriter("./test_cp.avi", cv2.VideoWriter_fourcc('D', 'I', 'V', 'X'), 15,
                      (np.int(width), np.int(height)), True)
while True:
    ret, frame = capture.read()
    if ret is True:
        cv2.imshow("video-input", frame)
        out.write(frame)
        c = cv2.waitKey(50)
        if c == 27:  # ESC
            break
    else:
        break

capture.release()
out.release()
