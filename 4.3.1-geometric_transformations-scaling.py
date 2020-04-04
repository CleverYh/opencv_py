# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'pictures\cat.jpg')

res = cv2.resize(img,None,fx=1.5, fy=0.5, interpolation = cv2.INTER_CUBIC)

cv2.imshow("resize",res)
cv2.waitKey(0)
cv2.destroyAllWindows()

#OR

# height, width = img.shape[:2]
# res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)