import numpy as np
import cv2 as cv
img = cv.imread("imgs/messi.jpeg")



ball = img[ 407:511,263:367]
img[389:493, 135:239] = ball

#b,g,r = cv.split(img)
#cv.split() is a costly operation (in terms of time). So use it only if necessary. Otherwise go for Numpy indexing.
#or b = img[:,:,0]
#print(b)
#print(g)
#img = cv.merge((b,g,r))

while(1):
    cv.imshow('image',img)
    
    if cv.waitKey(20) & 0xFF == ord('s'):
        break
cv.destroyAllWindows()

