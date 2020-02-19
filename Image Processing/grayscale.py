import cv2
  
image = cv2.imread('bojack.jpg', 0)
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
cv2.imshow('Original image',image)
#cv2.imshow('Gray image', gray)
  
cv2.waitKey(0)
cv2.destroyAllWindows()
