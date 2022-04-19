
import cv2 as cv
img = cv.imread("imgs/peepo.jpg")
img2 = cv.imread("imgs/peepo2.jpg")

#takes path of pic and returns img matrix of pixels


cv.imshow("Peepo 2", img2)
while(1):
    if cv.waitKey(20) & 0xFF == ord('s'):
        print("hi")
        cv.imshow("Peepo", img)
    elif cv.waitKey(20) & 0xFF == ord('d'):
        print("ufbw")
        cv.imshow("Peepo2", img2)
    elif cv.waitKey(20) & 0xFF == ord('q'):
        break