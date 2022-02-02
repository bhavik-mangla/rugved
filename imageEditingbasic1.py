import numpy as np
import cv2 as cv
img = cv.imread("/Users/bhavikmangla/Downloads/peepo.jpg")

#takes path of pic and returns img matrix of pixels




print(img.item(10,10,2))

for i in range(10,50):
    for j in range (10,20):
        img.itemset((i,j,0),255)
        img.itemset((i,j,1),255)
        img.itemset((i,j,2),255)

print(img.item(10,10,2))

print( img.shape )

print( img.size )
#Total number of pixels

print( img.dtype )

cv.imshow("Peepo", img)
if cv.waitKey() == ord("s"):
    cv.imshow("Peepo", img)