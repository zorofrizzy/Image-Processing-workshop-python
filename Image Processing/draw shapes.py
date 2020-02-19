import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)


#change colour of image?
img[60:120] = [0,0,153]


# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),(255,255,0),5)



#Rec
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.imshow('img', img)

#circle
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

cv2.imshow('img2', img)

#text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'LoL',(10,500), font, 4,(0,255,255),2,cv2.LINE_AA)

cv2.imshow('xd', img)
cv2.waitKey(0)



"""
 Syntax:
 cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])




Parameters:

image: It is the image on which text is to be drawn.

text: Text string to be drawn.

org: It is the coordinates of the bottom-left corner of the
text string in the image. The coordinates are represented as
tuples of two values i.e. (X coordinate value, Y coordinate value).

font: It denotes the font type. Some of font types are
FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, , etc.

fontScale: Font scale factor that is multiplied by
the font-specific base size.

color: It is the color of text string to be drawn.
For BGR, we pass a tuple. eg: (255, 0, 0) for blue color.

thickness: It is the thickness of the line in px.

lineType: This is an optional parameter.It gives the
type of the line to be used.

bottomLeftOrigin: This is an optional parameter.
When it is true, the image data origin is at the
bottom-left corner. Otherwise, it is at the
top-left corner.
"""

