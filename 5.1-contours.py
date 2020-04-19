# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt


img = cv2.imread(r'pictures\cat.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_rgb = img
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img_gray,127,255,0)

# There are three arguments in cv2.findContours() function, first one is source image, second is contour retrieval mode, third is contour approximation method. And it outputs the image, contours and hierarchy. contours is a Python list of all the contours in the image. Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.
# Note Since opencv 3.2 source image is not modified by this function.
# image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #  not enough values to unpack (expected 3, got 2) in OpenCV 4, works in OpenCV 3
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # works in OpenCV 4

# To draw the contours, cv2.drawContours function is used. It can also be used to draw any shape provided you have its boundary points. Its first argument is source image, second argument is the contours which should be passed as a Python list, third argument is index of contours (useful when drawing individual contour. To draw all contours, pass -1) and remaining arguments are color, thickness etc.
cont_all = cv2.drawContours(img, contours, -1, (0,255,0), 3) # draw all the contours in an image

cont_4th = cv2.drawContours(img, contours, 3, (0,255,0), 3) # draw an individual contour, say 4th contour here
# the way below is the same as cont_4th but more useful
cnt = contours[4]
cont_4th_useful = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)

# Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity. The contours are a useful tool for shape analysis and object detection and recognition.

# 1. For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
# 2. findContours() function modifies the source image. So if you want source image even after finding contours, already store it to some other variables.
# 3. In OpenCV, finding contours is like finding white object from black background. So remember, object to be found should be white and background should be black.

# Contour Approximation Method is the third argument in cv2.findContours function. Above, we told that contours are the boundaries of a shape with same intensity. It stores the (x,y) coordinates of the boundary of a shape. But does it store all the coordinates ? That is specified by this contour approximation method. If you pass cv2.CHAIN_APPROX_NONE, all the boundary points are stored. But actually do we need all the points? For eg, you found the contour of a straight line. Do you need all the points on the line to represent that line? No, we need just two end points of that line. This is what cv2.CHAIN_APPROX_SIMPLE does. It removes all redundant points and compresses the contour, thereby saving memory.

plt.subplot(2, 2, 1), plt.imshow(img_rgb, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(cont_all, cmap='gray')
plt.title('contours_all'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(cont_4th, cmap='gray')
plt.title('contour_4th'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(cont_4th_useful, cmap='gray')
plt.title('contour_4th_useful'), plt.xticks([]), plt.yticks([])

plt.show()