#pylint:disable=no-member

import cv2 as cv

img = cv.imread('imgs/peepo.jpg')
cv.imshow('peepo', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
#sets pixel value to 0 if below 150, otherwise sets to 255
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY )
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV )
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding- tells the machine  which method to use wen computing optimal threshold value...
# (computes mean of neigbhourhood pixels of 11X11 kernel and finds opt. threshold values of that part)
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 20)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)