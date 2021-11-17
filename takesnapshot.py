import cv2
import dropbox
import time
import random

start_time = time.time()

def takesnapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        print(ret)
        cv2.imwrite("pic1.jpg",frame)
        result = False
    videoCaptureObject.release()
    cv2.destroyAllWindows()
takesnapshot()
