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
videoout = "goal"

cap = cv.VideoCapture(filepath)
counter = 0
def clip(start, duration=20):
    start_time = list(map(lambda k: (int(k[0]), int(k[1]), int(k[3]), int(k[4])), start))
    i = 0
    while i < len(start_time):

      while(cap.isOpened):
        ret, frame = cap.read()
        try:
            m1 = frame[38:62, 193: 205]
            m2 = frame[38:62, 204: 217]
            s1 = frame[38:62, 220: 232]
            s2 = frame[38:62, 231: 243]
            current = int(cap.get(0)/1000)
            time = get_time(m1, m2, s1, s2)
            a = "00:"+str(np.floor_divide(current, 60)).zfill(2)+":"+str(current%60)

            print(time, current, start_time, time==currentC)
            if time in start_time:
                counter+=1
                if counter == 3:
                    subprocess.run(["ffmpeg", "-ss", a, "-i", videoname, "-c", "copy", "-t", str(duration), videoout + str(time[0]) +str(time[1]) + str(time[2]) + str(time[3]) + ".mp4"])
                    i += 1

                    if (i >= len(start_time)):
                        break
            else:
                counter = 0
        except Exception as e:
            print(e)
            break

clip((["08:41", "40:00","02:54","14:23","22:23","30:15","30:48","33:59","37:45","38:24","39:95","43:38"]))
