# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

# So what is histogram ? You can consider histogram as a graph or plot, which gives you an overall idea about the intensity distribution of an image. It is a plot with pixel values (ranging from 0 to 255, not always) in X-axis and corresponding number of pixels in the image on Y-axis. You can find it on your cellphone gallery, camera, Photoshop and so on.

# Now we have an idea on what is histogram, we can look into how to find this. Both OpenCV and Numpy come with in-built function for this. Before using those functions, we need to understand some terminologies related with histograms.

# BINS : A histogram shows the number of pixels for every pixel value, ie from 0 to 255. ie you need 256 values to show it. But consider, what if you need not find the number of pixels for all pixel values separately, but number of pixels in a interval of pixel values? say for example, you need to find the number of pixels lying between 0 to 15, then 16 to 31, ..., 240 to 255. You will need only 16 values to represent the histogram. And that is what is shown in example given in OpenCV Tutorials on histograms.

# So what you do is simply split the whole histogram to 16 sub-parts and value of each sub-part is the sum of all pixel count in it. This each sub-part is called “BIN”. In first case, number of bins where 256 (one for each pixel) while in second case, it is only 16. BINS is represented by the term histSize in OpenCV docs.

# DIMS : It is the number of parameters for which we collect the data. In this case, we collect data regarding only one thing, intensity value. So here it is 1.

# RANGE : It is the range of intensity values you want to measure. Normally, it is [0,256], ie all intensity values.

# So now we use cv2.calcHist() function to find the histogram. Let’s familiarize with the function and its parameters :

# cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])

# images : it is the source image of type uint8 or float32. it should be given in square brackets, ie, “[img]”.
# channels : it is also given in square brackets. It the index of channel for which we calculate histogram. For example, if input is grayscale image, its value is [0]. For color image, you can pass [0],[1] or [2] to calculate histogram of blue,green or red channel respectively.
# mask : mask image. To find histogram of full image, it is given as “None”. But if you want to find histogram of particular region of image, you have to create a mask image for that and give it as mask. (I will show an example later.)
# histSize : this represents our BIN count. Need to be given in square brackets. For full scale, we pass [256].
# ranges : this is our RANGE. Normally, it is [0,256].

# Simply load an image in grayscale mode and find its full histogram.
img = cv2.imread(r'pictures\a.jpg',0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
# hist is a 256x1 array, each value corresponds to number of pixels in that image with its corresponding pixel value.

# Numpy also provides you a function, np.histogram(). So instead of calcHist() function, you can try below line :
hist,bins = np.histogram(img.ravel(),256,[0,256])
# hist is same as we calculated before. But bins will have 257 elements, because Numpy calculates bins as 0-0.99, 1-1.99, 2-2.99 etc. So final range would be 255-255.99. To represent that, they also add 256 at end of bins. But we don’t need that 256. Upto 255 is sufficient.

# Numpy has another function, np.bincount() which is much faster than (around 10X) np.histogram(). So for one-dimensional histograms, you can better try that. Don’t forget to set minlength = 256 in np.bincount. For example :
hist = np.bincount(img.ravel(),minlength=256)
# print(hist)

# Hote that OpenCV function is more faster than (around 40X) than np.histogram(). So stick with OpenCV function.
