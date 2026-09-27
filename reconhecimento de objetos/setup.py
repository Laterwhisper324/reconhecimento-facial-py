import cv2
import reconhecimentoDeFrames
import mediapipe as mp


cap = cv2.VideoCapture(0)
face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        crop = frame[y:y + h, x:x + w]
        cv2.imwrite("face.jpg", crop)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eyes_cascade.detectMultiScale(roi_gray, 1.3, 5)

        if len(eyes) == 0:
            print("no eyes")
        else:
            # As coordenadas dos olhos são relativas ao recorte do rosto.
            eye_x1 = min(ex for ex, ey, ew, eh in eyes)
            eye_y1 = min(ey for ex, ey, ew, eh in eyes)
            eye_x2 = max(ex + ew for ex, ey, ew, eh in eyes)
            eye_y2 = max(ey + eh for ex, ey, ew, eh in eyes)
            eyes_crop = roi_color[eye_y1:eye_y2, eye_x1:eye_x2]
            cv2.imwrite("olhos.jpg", eyes_crop)


        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)


    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
