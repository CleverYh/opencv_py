# coding: utf-8
import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

# OpenCV implementation is based on Robust Detection of Lines Using the Progressive Probabilistic Hough Transform by Matas, J. and Galambos, C. and Kittler, J.V.. The function used is cv2.HoughLinesP(). It has two new arguments.
# minLineLength - Minimum length of line. Line segments shorter than this are rejected.
# maxLineGap - Maximum allowed gap between line segments to treat them as single line.
# Best thing is that, it directly returns the two endpoints of lines. In previous case, you got only the parameters of lines, and you had to find all the points.

img = cv2.imread(r'pictures\sudoku.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)
# for x1,y1,x2,y2 in lines[0]:
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# cv2.imwrite('houghlines5.jpg',img)
plt.imshow(img, cmap='gray')
plt.title('houghlinesP'), plt.xticks([]), plt.yticks([])
plt.show()
