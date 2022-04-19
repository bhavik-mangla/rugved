
import numpy as np
import cv2 as cv
img = cv.imread("first.jpg")
print(img.shape)


def coords(event,x,y,flags,param):
    
    if event == 1:
        print(x,y)

cv.namedWindow('image')
cv.setMouseCallback('image',coords)

while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()


