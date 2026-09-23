import cv2
import numpy as np

cap = cv2.VideoCapture(0)

print("--------------------------")
print("1-linhas")
print("2-retangulo")
print("3-circulo")
print("4-texto")
print("--------------------------")
escolha = input("Qual a sua escolha: ")

#auhybdaubdwaj
print(escolha)

match escolha:
    case "1":
        while True:
            ret, frame = cap.read()
            width = int(cap.get(3))
            height = int(cap.get(4))

            # linhas nas horizontais e verticais
            # posição inicial - posição final - cor - borda

            img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
            img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 10)
            img = cv2.line(img, (width//2, 0), (width//2, height), (0, 0, 255), 10)
            img = cv2.line(img, (0, height//2), (width, height//2), (0, 0, 0), 10)

            cv2.imshow("Frame", frame)

            if cv2.waitKey(1) == ord("q"):
                break

    case "2":
        while True:
            ret, frame = cap.read()
            width = int(cap.get(3))
            height = int(cap.get(4))

            # retangulo no meio: posição inicial: (x//2 - 100 - y//2 - 100) posição final: (x//2 + 100 - y//2+100)
            img = cv2.rectangle(frame, (220, 140) , (420, 340), (128, 128, 128), -1)

            cv2.imshow("Frame", frame)

            if cv2.waitKey(1) == ord("q"):
                break


    case "3":
        while True:
            ret, frame = cap.read()
            width = int(cap.get(3))
            height = int(cap.get(4))

            # circulo:
            img = cv2.circle(frame, (320, 240), 60, (255, 0, 0), 1)

            cv2.imshow("Frame", frame)

            if cv2.waitKey(1) == ord("q"):
                break

    case "4":
        texto = input("Qual a sua texto: ")

        while True:
            ret, frame = cap.read()
            width = int(cap.get(3))
            height = int(cap.get(4))

            # textos: texto "bomdia", (x, y), font, tamanho, cor, borda, cv2.line_aa
            font = cv2.FONT_HERSHEY_SIMPLEX
            img = cv2.putText(frame, texto, (160, 240 -10), font, 4, (255,0,0), -1, cv2.LINE_AA)

            cv2.imshow("Frame", frame)

            if cv2.waitKey(1) == ord("q"):
                break






