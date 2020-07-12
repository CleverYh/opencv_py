# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

# In two-dimensional histograms, you consider two features. Normally it is used for finding color histograms where two features are Hue & Saturation values of every pixel.

# It is quite simple and calculated using the same function, cv2.calcHist(). For color histograms, we need to convert the image from BGR to HSV. (Remember, for 1D histogram, we converted from BGR to Grayscale). For 2D histograms, its parameters will be modified as follows:

# channels = [0,1] because we need to process both H and S plane.
# bins = [180,256] 180 for H plane and 256 for S plane.
# range = [0,180,0,256] Hue value lies between 0 and 180 & Saturation lies between 0 and 256.

img = cv2.imread(r'pictures\imL.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

# Numpy also provides a specific function for this : np.histogram2d(). (Remember, for 1D histogram we used np.histogram() ).

h,s,v = cv2.split(hsv)
hist, xbins, ybins = np.histogram2d(h.ravel(), s.ravel(), [180, 256], [[0, 180], [0, 256]])

# First argument is H plane, second one is the S plane, third is number of bins for each and fourth is their range.

# The result we get is a two dimensional array of size 180x256. So we can show them as we do normally, using cv2.imshow() function. It will be a grayscale image and it won’t give much idea what colors are there, unless you know the Hue values of different colors.

# We can use matplotlib.pyplot.imshow() function to plot 2D histogram with different color maps. It gives us much more better idea about the different pixel density. But this also, doesn’t gives us idea what color is there on a first look, unless you know the Hue values of different colors. Still I prefer this method. It is simple and better.
# Note that while using this function, remember, interpolation flag should be nearest for better results.

plt.imshow(hist, interpolation='nearest')
plt.show()

# Note that in numpy:
# ravel(): Return a contiguous flattened array. A 1-D array, containing the elements of the input, is returned. A copy is made only if needed.
# flatten(): Return a copy of the array collapsed into one dimension.
# squeeze()：Remove single-dimensional entries from the shape of an array.
