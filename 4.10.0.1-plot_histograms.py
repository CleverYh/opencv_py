# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

# Now we should plot histograms! There are two ways for this :
# Short Way : use Matplotlib plotting functions
# Long Way : use OpenCV drawing functions

# Matplotlib comes with a histogram plotting function : matplotlib.pyplot.hist()
# It directly finds the histogram and plot it. You need not use calcHist() or np.histogram() function to find the histogram. 

img = cv2.imread(r'pictures\a.2x.jpg',0)

plt.hist(img.ravel(),256,[0,256]); plt.show()

# Or you can use normal plot of matplotlib, which would be good for BGR plot. For that, you need to find the histogram data first.

img = cv2.imread(r'pictures\a.jpg')
color = ('b','g','r')
for i,col in enumerate(color): 
# class enumerate(iterable: Iterable[_T], start: int=...) 
# Return an enumerate object. 
    # iterable 
        # an object supporting iteration 
# The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.
# enumerate is useful for obtaining an indexed list
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
