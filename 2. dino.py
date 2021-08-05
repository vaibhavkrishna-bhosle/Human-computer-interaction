import cv2
import time
import os
import track as track
import pyautogui as control

wcam, hcam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4,hcam)
detector = track.handDetector(detectionCon=0.75)

ptime = 0
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)
    
    if len(lmlist) !=0:
        if (lmlist[8][2] < lmlist[6][2]) and (lmlist[12][2] < lmlist[10][2]) and (lmlist[16][2] < lmlist[14][2]) and (lmlist[20][2] < lmlist[18][2]):
            control.press('space')
                    
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv2.putText(img, f'FPS:{int(fps)}',(400,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)