# coding: utf-8
from cv2 import cv2
import numpy as np

img = cv2.imread(r'pictures\a.jpg')

cv2.namedWindow("Demo")
roi = img[600:1200, 2100:3600]  # 1500x600 (r=600,c=1500)
cv2.imshow("Demo", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow("Demo", 0)
cv2.imshow("Demo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow("Demo", 0)
b, g, r = cv2.split(img)
cv2.imshow("Demo", b)
cv2.waitKey(0)

img = cv2.merge((r, g, b))
cv2.imshow("Demo", img)
cv2.waitKey(0)

img = cv2.merge((b, g, r))
cv2.imshow("Demo", img)
cv2.waitKey(0)

img[0:600, 1000:2500] = roi
cv2.imshow("Demo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
