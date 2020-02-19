import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('bojack.jpg')

#AVERAGE BLUR - avg of pixels under kernel area



blur = cv2.blur(img,(5,5))



blur = cv2.GaussianBlur(img,(5,5),0)


median = cv2.medianBlur(img,5)
