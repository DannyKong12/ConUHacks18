import numpy as np
import cv2 as cv
from PIL import Image
from sklearn import datasets, svm, metrics
from PIL import Image
import pytesseract
import argparse
import os
import subprocess

# exec("ffmpeg -ss -i"+ filename + str(times[i]) + str(120) + outfilename)




templates = [cv.imread("./templates/"+str(i)+".png") for i in range(10)]

def get_time(m1, m2, s1, s2):
    m1 = cv.cvtColor(m1, cv.COLOR_BGR2GRAY)
    templateGray = [cv.cvtColor(i, cv.COLOR_BGR2GRAY) for i in templates]
    result = [cv.matchTemplate(m1,i, cv.TM_CCOEFF) for i in templateGray]
    m1 = [cv.minMaxLoc(i)[1] for i in result]
    m1 = np.argmax(m1)
    m2 = cv.cvtColor(m2, cv.COLOR_BGR2GRAY)
    templateGray = [cv.cvtColor(i, cv.COLOR_BGR2GRAY) for i in templates]
    result = [cv.matchTemplate(m2,i, cv.TM_CCOEFF) for i in templateGray]
    m2 = [cv.minMaxLoc(i)[1] for i in result]
    m2 = np.argmax(m2)
    s1 = cv.cvtColor(s1, cv.COLOR_BGR2GRAY)
    templateGray = [cv.cvtColor(i, cv.COLOR_BGR2GRAY) for i in templates]
    result = [cv.matchTemplate(s1,i, cv.TM_CCOEFF) for i in templateGray]
    s1 = [cv.minMaxLoc(i)[1] for i in result]
    s1 = np.argmax(s1)
    s2 = cv.cvtColor(s2, cv.COLOR_BGR2GRAY)
    templateGray = [cv.cvtColor(i, cv.COLOR_BGR2GRAY) for i in templates]
    result = [cv.matchTemplate(s2,i, cv.TM_CCOEFF) for i in templateGray]
    s2 = [cv.minMaxLoc(i)[1] for i in result]
    s2 = np.argmax(s2)
    return (m1, m2, s1, s2)

filepath = "./full_match.mp4"
videoname = "full_match.mp4"
videoout = "goal1.mp4"

cap = cv.VideoCapture(filepath)
counter = 0
def clip(start, duration=20):
    while(cap.isOpened()):
        ret, frame = cap.read()
        try:
            m1 = frame[36:64, 193: 205]
            m2 = frame[36:64, 204: 217]
            s1 = frame[36:64, 219: 231]
            s2 = frame[36:64, 231: 243]
            current = int(cap.get(0)/1000)
            time = get_time(m1, m2, s1, s2)
            start_time = (int(start[0]), int(start[1]), int(start[3]), int(start[4]))
            a = "00:"+str(np.floor_divide(current, 60)).zfill(2)+":"+str(current%60)
            print(time, current, start_time, time==start_time)
            if time == start_time:
                counter+=1
                if counter == 5:
                    subprocess.run(["ffmpeg", "-ss", a, "-i", videoname, "-c", "copy", "-t", str(duration), videoout])
                    print("You finally did it you dumbass fuck")
                    break
            else:
                counter = 0
        except Exception as e:
            print(e)
            print("you actual fucking autist jesus christ")
            break

clip("08:36")
