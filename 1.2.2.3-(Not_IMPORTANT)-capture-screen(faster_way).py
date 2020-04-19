import numpy as np
from cv2 import cv2
from mss import mss
from PIL import Image
import time

init_time = last_time = time.time()
count = 0

while 1:
    with mss() as sct:
        monitor = {'top': 40, 'left': 0, 'width': 800, 'height': 450}
        img = np.array(sct.grab(monitor))

        print('Loop took {} seconds ' .format(time.time()-last_time))
        count += 1
        last_time = time.time()

        cv2.imshow('test', np.array(img))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

print('each loop took avg {} seconds ' .format((last_time-init_time)/count))

# A faster way using mss  (Loop took about 0.06 seconds on my notebook instead of 0.10 seconds using ImageGrab)
# mss: 16.7fps             (capture BGR stream)
# PIL.ImageGrab: 10.0fps   (capture RGB stream)

# below is a 'more faster way' (as the provider said) but causes error on my notebook

# mon = {'top': 160, 'left': 160, 'width': 200, 'height': 200}

# with mss() as sct:

#     while 1:
#         sct.get_pixels(mon)
#         img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
#         cv2.imshow('test', np.array(img))
#         if cv2.waitKey(25) & 0xFF == ord('q'):
#             cv2.destroyAllWindows()
#             break
