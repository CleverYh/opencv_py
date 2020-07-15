# coding: utf-8
import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt

# Hough Transform is a popular technique to detect any shape, if you can represent that shape in mathematical form. It can detect the shape even if it is broken or distorted a little bit. We will see how it works for a line.

# A line can be represented as y = mx+c or in parametric form, as \rho = x \cos \theta + y \sin \theta where \rho is the perpendicular distance from origin to the line, and \theta is the angle formed by this perpendicular line and horizontal axis measured in counter-clockwise ( That direction varies on how you represent the coordinate system. This representation is used in OpenCV).

# So if line is passing below the origin, it will have a positive rho and angle less than 180. If it is going above the origin, instead of taking angle greater than 180, angle is taken less than 180, and rho is taken negative. Any vertical line will have 0 degree and horizontal lines will have 90 degree.

# Now let’s see how Hough Transform works for lines. Any line can be represented in these two terms, (\rho, \theta). So first it creates a 2D array or accumulator (to hold values of two parameters) and it is set to 0 initially. Let rows denote the \rho and columns denote the \theta. Size of array depends on the accuracy you need. Suppose you want the accuracy of angles to be 1 degree, you need 180 columns. For \rho, the maximum distance possible is the diagonal length of the image. So taking one pixel accuracy, number of rows can be diagonal length of the image.

# Consider a 100x100 image with a horizontal line at the middle. Take the first point of the line. You know its (x,y) values. Now in the line equation, put the values \theta = 0,1,2,....,180 and check the \rho you get. For every (\rho, \theta) pair, you increment value by one in our accumulator in its corresponding (\rho, \theta) cells. So now in accumulator, the cell (50,90) = 1 along with some other cells.

# Now take the second point on the line. Do the same as above. Increment the the values in the cells corresponding to (\rho, \theta) you got. This time, the cell (50,90) = 2. What you actually do is voting the (\rho, \theta) values. You continue this process for every point on the line. At each point, the cell (50,90) will be incremented or voted up, while other cells may or may not be voted up. This way, at the end, the cell (50,90) will have maximum votes. So if you search the accumulator for maximum votes, you get the value (50,90) which says, there is a line in this image at distance 50 from origin and at angle 90 degrees.

# Everything explained above is encapsulated in the OpenCV function, cv2.HoughLines(). It simply returns an array of (\rho, \theta) values. \rho is measured in pixels and \theta is measured in radians. First parameter, Input image should be a binary image, so apply threshold or use canny edge detection before finding applying hough transform. Second and third parameters are \rho and \theta accuracies respectively. Fourth argument is the threshold, which means minimum vote it should get for it to be considered as a line. Remember, number of votes depend upon number of points on the line. So it represents the minimum length of line that should be detected.

img = cv2.imread(r'pictures\sudoku.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

lines = cv2.HoughLines(edges, 1, np.pi/180, 180)
for line in lines:
    # for rho, theta in lines[0]: This is wrong. Only one line will be found through this way.
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# cv2.imwrite('houghlines3.jpg',img)
plt.imshow(img, cmap='gray')
plt.title('houghlines'), plt.xticks([]), plt.yticks([])
plt.show()
