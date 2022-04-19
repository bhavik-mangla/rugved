
import numpy as np
import cv2 as cv
img1 = cv.imread("imgs/peepo.jpg")
img2 = cv.imread("imgs/peepo2.jpg")

dst = cv.addWeighted(img1,0.75,img2,0.25,0)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows() 