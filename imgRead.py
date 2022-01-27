
import cv2 as cv
import sys
img = cv.imread("/Users/bhavikmangla/Downloads/peepo.jpg")
img2 = cv.imread("/Users/bhavikmangla/Downloads/peepo2.jpg")

#takes path of pic and returns img matrix of pixels


cv.imshow("Peepo", img)



if cv.waitKey() == ord("s"):
    cv.imshow("Peepo 2", img2)