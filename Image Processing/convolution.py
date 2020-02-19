import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bojack.jpg')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

cv2.imshow('óriginal', img )
cv2.imshow('blur', dst)


cv2.waitKey(0)
