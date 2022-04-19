import cv2 
import numpy as np 
import math

def regionOfInterest(image):
    
    height = image.shape[0]#y
    width = image.shape[1]#x

    # polygons = np.array([[(0, height), (int(width/2.5), 0), 
    #     (int(width/1.9), 0), (width, height)]])

    polygons= np.array([[(0, int(height/1.25)), (int(width/1.6), 0), 
        (int(width/2.4), 0), (width, int(height/1.25))]])
    
    zeroMask = np.zeros([height,width,1], np.uint8)
    img = cv2.fillConvexPoly(zeroMask, polygons,color=(255,255,255))
    cv2.imshow("img",img)
    # image = np.uint8(image)
    # img=np.uint8(img)
    # print(image)
    # print(img)

    cv2.imwrite("imgsdcesffff.jpg", img)
    print(img.shape)
    # img1 = cv2.resize(image, (400, 400), interpolation=cv2.INTER_CUBIC)
    # img2 = cv2.resize(img, (400, 400), interpolation=cv2.INTER_CUBIC)
    roi = cv2.bitwise_and(image, image, mask = img)

    return roi


fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

vid = cv2.VideoCapture('lane_vgt.mp4')
count = 0
while(vid.isOpened()):
    
    ret, frame = vid.read()
    cv2.imshow("original ", frame)
    
    roi = regionOfInterest(frame)
    cv2.imshow("original frame", roi)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    
vid.release()
out.release()