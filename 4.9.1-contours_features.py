# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

img_rgb = cv2.imread(r'pictures\paint.png')
img_rgb2 = img_rgb.copy()
img_rgb3 = img_rgb.copy()
img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img, 127, 255, 0)

contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]

# The function cv2.moments() gives a dictionary of all moment values calculated.
M = cv2.moments(cnt)
# print(M)

# You can extract useful data like area, centroid etc. Centroid is given by the relations, C_x = \frac{M_{10}}{M_{00}} and C_y = \frac{M_{01}}{M_{00}}.
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

# Contour Area is given by the function cv2.contourArea() or from moments, M[‘m00’].
area = cv2.contourArea(cnt)
# print(area)

# Contour Perimeter is also called arc length. It can be found out using cv2.arcLength() function. Second argument specify whether shape is a closed contour (if passed True), or just a curve.
perimeter = cv2.arcLength(cnt, True)
# print(perimeter)

# Contour Approximation approximates a contour shape to another shape with less number of vertices depending upon the precision we specify.
epsilon = 0.05*cv2.arcLength(cnt, True)

# The second argument is called epsilon, which is maximum distance from contour to approximated contour. It is an accuracy parameter.
approx = cv2.approxPolyDP(cnt, epsilon, True)
approx2 = cv2.approxPolyDP(cnt, 0.1*epsilon, True)

# Convex Hull will look similar to contour approximation, but it is not (Both may provide same results in some cases). Here, cv2.convexHull() function checks a curve for convexity defects and corrects it. Generally speaking, convex curves are the curves which are always bulged out, or at-least flat. And if it is bulged inside, it is called convexity defects.
# points are the contours we pass into.
# hull is the output, normally we avoid it.
# clockwise : Orientation flag. If it is True, the output convex hull is oriented clockwise. Otherwise, it is oriented counter-clockwise.
# returnPoints : By default, True. Then it returns the coordinates of the hull points. If False, it returns the indices of contour points corresponding to the hull points.
hull = cv2.convexHull(cnt)

# Check if a curve is convex or not.
k = cv2.isContourConvex(cnt)
print(k)

draw_approx = cv2.drawContours(img_rgb, [approx], 0, (0, 255, 0), 5)

draw_approx2 = cv2.drawContours(img_rgb2, [approx2], 0, (100, 190, 255), 5)

draw_approx3 = cv2.drawContours(img_rgb3, [hull], 0, (0, 255, 255), 5)
# image must be rgb or you'll get black contours which cannot be easily recognized.

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(draw_approx, cmap='gray')
plt.title('epsilon = 5% of the arc length'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(draw_approx2,cmap = 'gray')
plt.title('epsilon = 0.5% of the arc length'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(draw_approx3,cmap = 'gray')
plt.title('draw hull'), plt.xticks([]), plt.yticks([])

plt.show()
