import numpy as np

import os

import cv2

filename = 'kk.mp4'

frames_per_second = 25.0

my_res = '720p'

def change_res(cap, width, height):

    cap.set(3, width)
    cap.set(4, height)

STD_DIMENSIONS = {

"480p": (640, 480),
"720p": (1280, 720),
"1080p": (1920, 1080),
"4k": (3840, 2160),
}

def get_dims(cap, res='1080p'):

    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    change_res(cap, width, height)
    return width, height

VIDEO_TYPE = {

'avi': cv2.VideoWriter_fourcc(*'XVID'),
'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}

def get_video_type(filename):

    filename, ext = os.path.splitext(filename)
    if ext in VIDEO_TYPE:
        return  VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']

cap = cv2.VideoCapture(0)


out = cv2.VideoWriter(filename, get_video_type(filename), frames_per_second, get_dims(cap, my_res))

while True:

    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv2.flip(frame, 1)

    # # Converting to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # # Blur 
    # blur = cv2.GaussianBlur(gray, (3,3), cv2.BORDER_DEFAULT)
    # # Edge Cascade
    # canny = cv2.Canny(blur, 125, 175)
    # # Dilating the image
    # dilated = cv2.dilate(canny, (7,7), iterations=3)
    blank = np.zeros(frame.shape, dtype='uint8')
    ret, thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
    contours, hierarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    print(f'{len(contours)} contour(s) found!')

    cv2.drawContours(blank, contours, -1, (0,0,255), 1)

    # write the flipped frame
    out.write(blank)

    cv2.imshow('frame',blank)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

out.release()

cv2.destroyAllWindows()