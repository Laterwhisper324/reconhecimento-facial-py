import cv2
import random
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = np.zeros(frame.shape, np.uint8)

    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    img[:height//2, :width//2] = cv2.cvtColor(small_frame, cv2.COLOR_BGR2LAB)
    img[height//2:, :width//2] = small_frame
    img[:height//2, width//2:] = cv2.rotate(small_frame, cv2.ROTATE_180)
    img[height//2:, width//2:] = small_frame

    cv2.imshow("Frame", img)

    if cv2.waitKey(1) == ord("q"):
        break