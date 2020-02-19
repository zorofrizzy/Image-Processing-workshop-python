import cv2
import numpy as np


bojack = cv2.imread('bojack.jpg')
batman = cv2.imread('test1.jpg')


height1, width1, _ = bojack.shape
height2, width2, _ = batman.shape

height = min(height1, height2)
width = min(width1, width2)

bojack = bojack[:height, :width]
batman = batman[:height, :width]

cv2.imshow('bat', batman)
cv2.imshow('bojack', bojack)
"""

numpyAdd = batman + bojack

cvAdd = cv2.add(batman, bojack)

cv2.imshow('CV2 Add', cvAdd)
cv2.imshow('NUmpy add', numpyAdd)

"""


dst = cv2.addWeighted(batman, 0.7, bojack,0.3, 34)
cv2.imshow('dst', dst)

dest = cv2.addWeighted(batman, 0.5, bojack,0.5, 3)
cv2.imshow('dest', dest)


cv2.waitKey(0)






