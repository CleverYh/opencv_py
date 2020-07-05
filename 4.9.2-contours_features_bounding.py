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

# Straight Bounding Rectangle is a straight rectangle, it doesn’t consider the rotation of the object. So area of the bounding rectangle won’t be minimum. It is found by the function cv2.boundingRect().

# Let (x,y) be the top-left coordinate of the rectangle and (w,h) be its width and height.
x, y, w, h = cv2.boundingRect(cnt)
boundingRect = cv2.rectangle(img_rgb, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Rotated Rectangle is drawn with minimum area, so it considers the rotation also. The function used is cv2.minAreaRect(). It returns a Box2D structure which contains following detals - (top-left corner(x, y), (width, height), angle of rotation). But to draw this rectangle, we need 4 corners of the rectangle. It is obtained by the function cv2.boxPoints()
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
boundingRect = cv2.drawContours(img_rgb, [box], 0, (0, 0, 255), 2)

# cv2.minEnclosingCircle() find the circumcircle of an object. It is a circle which completely covers the object with minimum area.
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
circumcircle = cv2.circle(img_rgb2, center, radius, (0, 255, 0), 2)

# To fit an ellipse to an object, use the function cv2.fitEllipse(). It returns the rotated rectangle in which the ellipse is inscribed.
ellipse = cv2.fitEllipse(cnt)
fit = cv2.ellipse(img_rgb3, ellipse, (0, 255, 0), 2)

# Similarly we can fit a line to a set of points. Below image contains a set of white points. We can approximate a straight line to it.
rows, cols = img.shape[:2]
[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
fit = cv2.line(img_rgb3, (cols-1, righty), (0, lefty), (0, 255, 0), 2)


plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(boundingRect, cmap='gray')
plt.title('boundingRect and RotatedRect'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(circumcircle, cmap='gray')
plt.title('minEnclosingCircle'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(fit, cmap='gray')
plt.title('fit ellipse and line'), plt.xticks([]), plt.yticks([])

plt.show()
