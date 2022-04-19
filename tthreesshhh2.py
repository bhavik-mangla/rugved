

import cv2
import numpy as np
cap = cv2.VideoCapture("lane_vgt.mp4")
while(cap.isOpened()):
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 9)
    cv2.imshow('Adaptive Thresholding', adaptive_thresh)
    threshold, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY )
    cv2.imshow('Simple Thresholded', thresh)
#1- (hMin = 49 , sMin = 39, vMin = 144), (hMax = 91 , sMax = 101, vMax = 255)

# image = cv2.blur(image,(5,5))
# #(hMin = 44 , sMin = 54, vMin = 137), (hMax = 99 , sMax = 136, vMax = 158)

#2- hMin = 39 , sMin = 51, vMin = 150), (hMax = 65 , sMax = 91, vMax = 216) 

#3- (hMin = 29 , sMin = 38, vMin = 155), (hMax = 71 , sMax = 80, vMax = 231)----
    # Set minimum and max HSV values to display
#4- (hMin = 51 , sMin = 47, vMin = 152), (hMax = 63 , sMax =
# []- 88, vMax = 255)

#5- hMin = 51 , sMin = 57, vMin = 155), (hMax = 73 , sMax = 255, vMax = 255)
    
    lower = np.array([51, 57, 155])
    upper = np.array([73, 255, 255])

    # Create HSV Image and threshold into a range.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(frame,frame, mask= mask)


    cv2.imshow('image',output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()