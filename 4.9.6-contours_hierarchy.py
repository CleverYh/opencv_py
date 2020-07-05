# coding: utf-8
import numpy as np
from cv2 import cv2
import matplotlib.pyplot as plt

# The hierarchy of contours is the parent-child relationship in Contours. In some cases, some shapes are inside other shapes. Just like nested figures. In this case, we call outer one as parent and inner one as child. This way, contours in an image has some relationship to each other. And we can specify how one contour is connected to each other, like, is it child of some other contour, or is it a parent etc. Representation of this relationship is called the Hierarchy.
# each contour has its own information regarding what hierarchy it is, who is its child, who is its parent etc. OpenCV represents it as an array of four values : [Next, Previous, First_Child, Parent]
# Next denotes next contour at the same hierarchical level. Previous denotes previous contour at the same hierarchical level. First_Child denotes its first child contour. Parent denotes index of its parent contour. If there is no child or parent, that field is taken as -1

img_rgb = cv2.imread(r'pictures\tree_hierarchy.png')
img = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img, 127, 255, 0)

# RETR_LIST is the simplest of the four flags (from explanation point of view). It simply retrieves all the contours, but doesn’t create any parent-child relationship. Parents and kids are equal under this rule, and they are just contours. ie they all belongs to same hierarchy level.
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print('RETR_LIST \n', hierarchy)

# RETR_EXTERNAL returns only extreme outer flags. All child contours are left behind. We can say, under this law, Only the eldest in every family is taken care of. It doesn’t care about other members of the family :)
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('RETR_EXTERNAL \n', hierarchy)

# RETR_CCOMP retrieves all the contours and arranges them to a 2-level hierarchy. ie external contours of the object (ie its boundary) are placed in hierarchy-1. And the contours of holes inside object (if any) is placed in hierarchy-2. If any object inside it, its contour is placed again in hierarchy-1 only. And its hole in hierarchy-2 and so on.
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
print('RETR_CCOMP \n', hierarchy)

# RETR_TREE retrieves all the contours and creates a full family hierarchy list. It even tells, who is the grandpa, father, son, grandson and even beyond... :)
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('RETR_TREE \n', hierarchy)
