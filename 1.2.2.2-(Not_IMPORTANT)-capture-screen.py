# coding: utf-8
import numpy as np
from PIL import ImageGrab
from cv2 import cv2
import time

count = 0
init_time = last_time = time.time()

while(1):
    printscreen_pil = ImageGrab.grab(bbox=(0, 50, 640, 480))

    count += 1
    print('Loop took {} seconds ' .format(time.time()-last_time))
    last_time = time.time()

    cv2.imshow('window', np.array(printscreen_pil))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

print('each loop took avg {} seconds ' .format((last_time-init_time)/count))

# 因为笔记本的摄像头坏了（不知道是驱动的问题还是硬件的问题，明明之前还能用的qwq），所以采用airplay+ImageGrab.grab()曲线救国，利用iPhone和iPad的摄像头做实验。
