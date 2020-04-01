from cv2 import cv2
import numpy as np

img = cv2.imread('a.jpg')

pixel = img[200, 200]
img[200, 200] = [255, 255, 255]
b = img[200, 200, 0]
g = img[200, 200, 1]
r = img[200, 200, 2]
r = img[200, 200, 2] = 1

print(img[200,200])
cv2.namedWindow("img", 0)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
