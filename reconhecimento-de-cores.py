import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Faixas de vermelho (o vermelho fica nas duas pontas da escala H)
lower_red1 = np.array([0, 100, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 100, 70])
upper_red2 = np.array([180, 255, 255])

# Faixa de azul
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Máscara vermelha: junta as duas faixas
    mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    # Máscara azul
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Aplica cada máscara no frame original
    result_red = cv2.bitwise_and(frame, frame, mask=mask_red)
    result_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)

    cv2.imshow("Vermelho", result_red)
    # mascara vermelha
    cv2.imshow("Vermelho-mascara", mask_red)

    cv2.imshow("Azul", result_blue)
    # mascara azul
    cv2.imshow("Azul-mascara", mask_blue)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()