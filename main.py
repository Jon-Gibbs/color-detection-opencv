import cv2
from PIL import Image
from util import get_limits
#this program accesses the machines webcam, takes the video captured by it, and displays it in a window onscreen

yellow = [0, 0, 0] # yellow in brg
#initialize a connection to the webcam and store that connection in the "cap" object
cap=cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() #captures a frame from the webcam and stores the image in the frame variable, ret is a boolean that returns true if the the image was captured properly, and false if not

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask )

    boundingBox = mask_.getbbox()

    if boundingBox is not None:
        x1,y1,x2,y2 = boundingBox

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 5)

    print(boundingBox)

    cv2.imshow('the guy' , frame) #takes the image stored in "frame" and posts it in the window using the cv2.imshow function

    if cv2.waitKey(1) & 0xFF == ord('q'): # breaks the loop is the user presses q
        break

cap.release() #releases the camera (a bit like calling destroy)

cv2.destroyAllWindows() #cleans up any hanging windows the program made


