import cv2
import numpy as np

#config
h_min = 0
h_max = 179
s_min = 0
s_max = 255
v_min = 0
v_max = 255

#functions
def getContours(img, reduceImg, originalImg):
    contours, hierachy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        print(area)
        if area > 500:
            cv2.drawContours(reduceImg, contour, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02*peri, True)
            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

            cv2.rectangle(reduceImg, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.rectangle(originalImg, (x, y), (x + w, y + h), (0, 255, 0), 2)


def updateGrayHSV():
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    reduceImg = cv2.bitwise_and(img, img, mask=mask)
    imgGrey = cv2.cvtColor(reduceImg, cv2.COLOR_BGR2GRAY);
    getContours(imgGrey, reduceImg, img)
    cv2.imshow("Original Video", img)
    cv2.imshow("Output Video", reduceImg)


def hMinTrackbar(pos):
    global h_min
    h_min = pos


def hMaxTrackbar(pos):
    global h_max
    h_max = pos


def sMinTrackbar(pos):
    global s_min
    s_min = pos


def sMaxTrackbar(pos):
    global s_max
    s_max = pos


def vMinTrackbar(pos):
    global v_min
    v_min = pos

def vMaxTrackbar(pos):
    global v_max
    v_max = pos

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)
cap.set(10, 150)

#create track bars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 600, 240)
cv2.createTrackbar("Hue Min", "TrackBars", h_min, 179,hMinTrackbar)
cv2.createTrackbar("Hue Max", "TrackBars", h_max, 179,hMaxTrackbar)
cv2.createTrackbar("Sat Min", "TrackBars", s_min, 255,sMinTrackbar)
cv2.createTrackbar("Sat Max", "TrackBars", s_max, 255,sMaxTrackbar)
cv2.createTrackbar("Val Min", "TrackBars", v_min, 255,vMinTrackbar)
cv2.createTrackbar("Val Max", "TrackBars", v_max, 255,vMaxTrackbar)

while True:
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    updateGrayHSV()
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break