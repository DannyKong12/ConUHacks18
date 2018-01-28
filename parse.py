import numpy as np
import cv2 as cv
from PIL import Image
from sklearn import datasets, svm, metrics
from PIL import Image
import pytesseract
import argparse
import os


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

filepath = "./first_goal.mp4"

cap = cv.VideoCapture(filepath)

counter = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    m1 = frame[36:64, 193: 205]
    m2 = frame[36:64, 204: 217]
    s1 = frame[36:64, 219: 231]
    s2 = frame[36:64, 231: 243]

    time = get_time(m1, m2, s1, s2)
    print("%d%d:%d%d" % time)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    edged = cv.Canny(blurred, 50, 200, 255)
    inv = cv.subtract(255, edged)
    cv.imshow('frame', inv)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# text = pytesseract.image_to_string(inv)
# print(text)

#search for the fucking clock here using clock img


# image = cv.imread(image)
# gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#
# # check to see if we should apply thresholding to preprocess the
# # image
# if args["preprocess"] == "thresh":
# 	gray = cv.threshold(gray, 0, 255,
# 		cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
#
# # make a check to see if median blurring should be done to remove
# # noise
# elif args["preprocess"] == "blur":
# 	gray = cv.medianBlur(gray, 3)
#
# # write the grayscale image to disk as a temporary file so we can
# # apply OCR to it
# filename = "{}.png".format(os.getpid())
# cv.imwrite(filename, gray)
#
# # load the image as a PIL/Pillow image, apply OCR, and then delete
# # the temporary file
# text = pytesseract.image_to_string(Image.open(filename))
# os.remove(filename)
# print(text)
#
# # show the output images
# cv.imshow("Image", image)
# cv.imshow("Output", gray)
# cv.waitKey(0)
