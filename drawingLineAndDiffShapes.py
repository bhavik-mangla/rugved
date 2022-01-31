import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(80,300),(255,0,0),5)
# x1,y1 ... x2,y2.... colour.....thickness

cv.rectangle(img,(200,0),(400,200),(0,255,0),4)
# top-left corner.... bottom-right corner....

cv.circle(img,(300,200), 63, (0,0,255), -1)
#center...radius...(-1 denotes filed color)

cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
#cv.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]	)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))
#draw a small polygon of with four vertices in yellow color.


font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
#cv.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]	
cv.imshow('frame', img)
cv.waitKey(0)


