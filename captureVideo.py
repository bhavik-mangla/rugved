
import cv2 as cv
# capture= cv.VideoCapture(0)  

# to capture ur camera....(if there were more cameras connected u can use 1, 2)


capture= cv.VideoCapture("/Users/bhavikmangla/Downloads/Gauss Elimination Method-20211111_094217-Meeting Recording.mp4")  


while True:
    isTrue, frame  = capture.read() #reads video frame by frame
    cv.imshow("Video",frame) #displaying individual frames
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        #to stop video playing for forever
        break

capture.release()
cv.destroyAllWindows()

