def recorte():
    import cv2
    import numpy as np
    import random


    cap = cv2.VideoCapture(0)

    #cria a camera e mostra os frames enquanto o while for true
    while True:
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    #gera um valor aleatorio no range de 1 ao tamanho da camera
    x1 = random.randint(1, width)
    y1 = random.randint(1, height)
    x2 = x1 + width
    y2 = y1 + height

    #desenha o retangulo

    img = cv2.rectangle(frame, (x1, y1), (x2, y2), (128, 128, 128), 1)
    #recorta ele com base nos valores do tamanho do retangulo

    crop = frame[y1:y2 , x1:x2]

    cv2.imwrite("frame.jpg", frame)
    cv2.imwrite("template.png", crop)
    cv2.imshow("Frame", crop)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
