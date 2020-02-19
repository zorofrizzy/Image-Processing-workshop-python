import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bojack.jpg',0)
edges = cv2.Canny(img,100,200)
cv2.imshow('canny', edges)

cv2.waitKey(0)
