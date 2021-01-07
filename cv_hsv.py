import cv2
import numpy as np

#what is HSV: https://en.wikipedia.org/wiki/HSL_and_HSV
#image classification: https://www.datasciencecentral.com/profiles/blogs/image-classification-with-hsv-color-model-processing

#config
path = 'Resources/dog_1.jpg'

h_min = 0
h_max = 179
s_min = 0
s_max = 255
v_min = 0
v_max = 255

#functions
def updateGrayHSV():
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    cv2.imshow("Mask", mask)
    reduceImg = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Result", reduceImg)

def hMinTrackbar(pos):
    global h_min
    h_min = pos
    print(h_min)
    updateGrayHSV()


def hMaxTrackbar(pos):
    global h_max
    h_max = pos
    print(h_max)
    updateGrayHSV()


def sMinTrackbar(pos):
    global s_min
    s_min = pos
    print(h_min)
    updateGrayHSV()


def sMaxTrackbar(pos):
    global s_max
    s_max = pos
    print(s_max)
    updateGrayHSV()


def vMinTrackbar(pos):
    global v_min
    v_min = pos
    print(v_min)
    updateGrayHSV()


def vMaxTrackbar(pos):
    global v_max
    v_max = pos
    print(v_max)
    updateGrayHSV()





#create track bars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 600, 240)
cv2.createTrackbar("Hue Min", "TrackBars", h_min, 179,hMinTrackbar)
cv2.createTrackbar("Hue Max", "TrackBars", h_max, 179,hMaxTrackbar)
cv2.createTrackbar("Sat Min", "TrackBars", s_min, 255,sMinTrackbar)
cv2.createTrackbar("Sat Max", "TrackBars", s_max, 255,sMaxTrackbar)
cv2.createTrackbar("Val Min", "TrackBars", v_min, 255,vMinTrackbar)
cv2.createTrackbar("Val Max", "TrackBars", v_max, 255,vMaxTrackbar)

#create two image version: original and hsv
img = cv2.imread(path)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#get h s v values



cv2.imshow("Original", img)
cv2.imshow("HSV", imgHSV)

cv2.waitKey(0)