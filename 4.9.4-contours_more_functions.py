# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'pictures\star.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 2, 1)
cnt = contours[0]

hull = cv2.convexHull(cnt, returnPoints=False)
# Remember we have to pass returnPoints = False while finding convex hull, in order to find convexity defects.
defects = cv2.convexityDefects(cnt, hull)
# It returns an array where each row contains these values - [ start point, end point, farthest point, approximate distance to farthest point ].


dist = cv2.pointPolygonTest(cnt, (50, 50), True)
# This function finds the shortest distance between a point (50, 50) in the image and a contour. It returns the distance which is negative when point is outside the contour, positive when point is inside and zero if point is on the contour.
# In the function, third argument is measureDist. If it is True, it finds the signed distance. If False, it finds whether the point is inside or outside or on the contour (it returns +1, -1, 0 respectively). Making it False gives about 2-3X speedup.

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end, [0, 255, 0], 2)
    cv2.circle(img, far, 5, [0, 0, 255], -1)

cv2.namedWindow("img", 0)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Exercises
# 1. Check the documentation for cv2.pointPolygonTest(), you can find a nice image in Red and Blue color. It represents the distance from all pixels to the white curve on it. All pixels inside curve is blue depending on the distance. Similarly outside points are red. Contour edges are marked with White. So problem is simple. Write a code to create such a representation of distance.
dist = np.zeros((img.shape[0], img.shape[1]), np.int8)
dist_im = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        dist[i, j] = cv2.pointPolygonTest(cnt, (i, j), True)
print(dist)
min, max, minLoc, maxLoc = cv2.minMaxLoc(dist)
min = abs(min)
max = abs(max)
print(min, max)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if(dist[i, j] < 0):
            dist_im[i, j, 0] = 255-int(abs(dist[i, j])*255)/min
        elif(dist[i, j] > 0):
            dist_im[i, j, 2] = 255-int(abs(dist[i, j])*255)/min
        else:
            dist_im[i, j] = [255, 0, 255]

cv2.namedWindow("img", 0)
cv2.imshow('img', dist_im)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. Compare images of digits or letters using cv2.matchShapes(). ( That would be a simple step towards OCR )
# 太简单不做了睡大觉
