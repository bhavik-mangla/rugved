import numpy as np
import cv2 as cv
# mouse callback function
def draw_circle(event,x,y,flags,param):
    print(event)
    if event == cv.EVENT_LBUTTONUP:
#Or if event == 4:
        cv.circle(img,(x,y),100,(255,0,0),-1)
#https://docs.opencv.org/3.4/d0/d90/group__highgui__window__flags.html
# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()