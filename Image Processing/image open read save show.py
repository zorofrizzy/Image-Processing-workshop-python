import cv2

import numpy as np

image = cv2.imread('test1.jpg')

cv2.imshow('Batman image test', image)

cv2.imwrite('lol.jpg', image)
cv2.waitKey(0)
