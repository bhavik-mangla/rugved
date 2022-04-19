

import cv2
import numpy as np
line_1 =[]
def make_points(image, line):
    try:
        slope, intercept = line
    except TypeError:
        slope, intercept = 5.499,-500
    try:
        y1 = int(image.shape[0])# bottom of the image
        y2 = int(y1*3/5)         # slightly lower than the middle
        x1 = int((y1 - intercept)/slope)
        x2 = int((y2 - intercept)/slope)
    except:
        y1 = 288
        y2 =480
        x1 = 137
        x2=154
    return [[x1, y1, x2, y2]]

def average_slope_intercept(image, lines):
    left_fit    = []
    right_fit   = []
    if lines is None:
        return None
    for line in lines:
        for x1, y1, x2, y2 in line:
            fit = np.polyfit((x1,x2), (y1,y2), 1)
            slope = fit[0]
            intercept = fit[1]
            if slope < 0: # y is reversed in image
                left_fit.append((slope, intercept))
            else:
                right_fit.append((slope, intercept))
    # add more weight to longer lines
    left_fit_average  = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    left_line  = make_points(image, left_fit_average)
    right_line = make_points(image, right_fit_average)
    averaged_lines = [left_line, right_line]
    return averaged_lines

def canny(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    kernel = 5
    blur = cv2.GaussianBlur(gray,(kernel, kernel),0)
    canny = cv2.Canny(gray, 50, 150)
    return canny

def display_lines(img,lines):
    line_image = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                print(x1, y1, x2, y2)
                x1=int(x1)
                x2=int(x2)
                y1=int(y1)
                y2=int(y2)
                try:
                    line_1 = cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
                    return line_1
                
                except:
                    return cv2.line(line_image,(137,154),(288,480),(255,0,0),10)
   

                

def region_of_interest(image):

    height = image.shape[0]#y
    width = image.shape[1]#x

    polygons= np.array([[(8,int(height/1.5)), (int(width/4.5), int(height/2)), 
        (int(width/1.5), int( height/2)), (582, int( height/1.5))]])
    
    mask = np.zeros_like(image)
    
    cv2.fillPoly(mask,polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    cv2.imshow("imggggg",image)
    return masked_image


    


# image = cv2.imread('test_image.jpg')
# lane_image = np.copy(image)
# lane_canny = canny(lane_image)
# cropped_canny = region_of_interest(lane_canny)
# lines = cv2.HoughLinesP(cropped_canny, 2, np.pi/180, 100, np.array([]), minLineLength=40,maxLineGap=5)
# averaged_lines = average_slope_intercept(image, lines)
# line_image = display_lines(lane_image, averaged_lines)
# combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 0)

#
cap = cv2.VideoCapture("lane_vgt.mp4")
while(cap.isOpened()):
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 9)
    cv2.imshow('Adaptive Thresholding', adaptive_thresh)
    threshold, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY )
    cv2.imshow('Simple Thresholded', thresh)
#(hMin = 49 , sMin = 39, vMin = 144), (hMax = 91 , sMax = 101, vMax = 255)

    # Set minimum and max HSV values to display
    lower = np.array([49, 39, 144])
    upper = np.array([91, 101, 255]) 


    # Create HSV Image and threshold into a range.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(frame,frame, mask= mask)

    cropped_canny = region_of_interest(output)
    lines = cv2.HoughLinesP(cropped_canny, 2, np.pi/180, 100, np.array([]), minLineLength=40,maxLineGap=5)
    averaged_lines = average_slope_intercept(frame, lines)
    line_image = display_lines(frame, averaged_lines)
    
    combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)

    cv2.imshow("result", combo_image)

    cv2.imshow('image',output)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
