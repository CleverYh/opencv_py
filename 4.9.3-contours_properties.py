# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

img_rgb = cv2.imread(r'pictures\bounding.png')
img_rgb2 = img_rgb.copy()
img_rgb3 = img_rgb.copy()
img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img, 127, 255, 0)

contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]

x, y, w, h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h
print('Aspect_ratio:', aspect_ratio)
# Aspect Ratio is the ratio of width to height of bounding rect of the object.

area = cv2.contourArea(cnt)

x, y, w, h = cv2.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area
print('Extent:', aspect_ratio)
# Extent is the ratio of contour area to bounding rectangle area.

hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area
print('Solidity:', aspect_ratio)
# Solidity is the ratio of contour area to its convex hull area.

equi_diameter = np.sqrt(4*area/np.pi)
print('Equivalent_diameter:', aspect_ratio)
# Equivalent Diameter is the diameter of the circle whose area is same as the contour area.

(x, y), (MA, ma), angle = cv2.fitEllipse(cnt)
print('x:', x, 'y:', y, '\n', 'MA:', MA, 'ma:', ma, '\n', 'angle:', angle)
# Orientation is the angle at which object is directed. Above method also gives the Major Axis and Minor Axis lengths.

mask = np.zeros(img.shape, np.uint8)
cv2.drawContours(mask, [cnt], 0, 255, -1)
pixelpoints = np.transpose(np.nonzero(mask))  # using Numpy functions
# pixelpoints = cv2.findNonZero(mask) # using OpenCV function
# Numpy gives coordinates in (row, column) format, while OpenCV gives coordinates in (x,y) format. So basically the answers will be interchanged. row = x and column = y.

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(img, mask=mask)
print(min_val, max_val, min_loc, max_loc)
# Maximum Value, Minimum Value and their locations

mean_val = cv2.mean(img, mask=mask)
# Find the average color of an object. Or it can be average intensity of the object in grayscale mode. Use the same mask to do it.

leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
print(leftmost, rightmost, topmost, bottommost)
# Extreme Points means topmost, bottommost, rightmost and leftmost points of the object.
