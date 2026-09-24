import cv2
import numpy as np

def capture():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) == ord("q"):
            break