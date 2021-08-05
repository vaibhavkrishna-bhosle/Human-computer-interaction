import cv2
import time
import os
import track as track
import pyautogui as control
import time

wcam, hcam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4,hcam)

detector = track.handDetector(detectionCon=0.75)

def check(lmlist):

    if len(lmlist) !=0:
        index_up    = lmlist[8][2] < lmlist[6][2]
        middle_up   = lmlist[12][2] < lmlist[10][2]
        ring_up     = lmlist[16][2] < lmlist[14][2]
        pinky_up  = lmlist[20][2] < lmlist[18][2]
        thumb_up = lmlist[4][1] < lmlist[2][1]


        index_down  = lmlist[8][2] > lmlist[6][2]
        middle_down = lmlist[12][2] > lmlist[10][2]
        ring_down   = lmlist[16][2] > lmlist[14][2]
        pinky_down  = lmlist[20][2] > lmlist[18][2]
        thumb_down = lmlist[4][1] > lmlist[2][1]

        if index_up and middle_down and ring_down and pinky_down and thumb_down:
            control.press("1")
            cv2.putText(img, "1",(400,70), cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
        elif index_up and middle_up and ring_down and pinky_down and thumb_down:
            control.press("2")
            cv2.putText(img, "2",(400,70), cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
        elif index_up and middle_up and ring_up and pinky_down and thumb_down:
            control.press("3")
            cv2.putText(img, "3",(400,70), cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
        elif index_up and middle_up and ring_up and pinky_up and thumb_down:
            control.press("4")
            cv2.putText(img, "4",(400,70), cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
        elif index_down and middle_down and ring_down and pinky_down and thumb_up:
            control.press("5")
            cv2.putText(img, "5",(400,70), cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
        elif index_up and middle_down and ring_down and pinky_down and thumb_up:
            control.press("6")
            cv2.putText(img, "6",(400,70), cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
        elif index_up and middle_up and ring_down and pinky_down and thumb_up:
            control.press("7")
            cv2.putText(img, "7",(400,70), cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
        elif index_up and middle_up and ring_up and pinky_down and thumb_up:
            control.press("8")
            cv2.putText(img, "8",(400,70), cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
        elif index_up and middle_up and ring_up and pinky_up and thumb_up:
            control.press("9")
            cv2.putText(img, "9",(400,70), cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
        elif index_down and middle_down and ring_down and pinky_down and thumb_down:
            control.press("0") 
            cv2.putText(img, "0",(400,70), cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
        else:
            print("not recognised")

while True:
    time.sleep(1)
    success, img = cap.read()
    img = cv2.flip(img,1)
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)

    check(lmlist)

    cv2.imshow("Image",img)
    cv2.waitKey(1)