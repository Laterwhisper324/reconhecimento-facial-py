import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    cv2.imshow("Frame", hls)

    if cv2.waitKey(1) == ord("q"):
        break