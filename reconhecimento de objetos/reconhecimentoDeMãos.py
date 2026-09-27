from pathlib import Path
from urllib.request import urlretrieve
import numpy as np
import cv2
import mediapipe as mp
import random
import pygame


MODEL_URL = (
    "https://storage.googleapis.com/mediapipe-models/hand_landmarker/"
    "hand_landmarker/float16/1/hand_landmarker.task"
)

pygame.mixer.init()
fart = pygame.mixer.Sound("fart.mp3")  # ou .mp3

MODEL_PATH = Path(__file__).with_name("hand_landmarker.task")

arrayPath = [
    "middle_finger_dog.jpg",
    "cat_middle_finger.jpg",
    "skull_middle_finger.jpg",
    "horse_middle_finger.jpg",
]


# Ligações entre os 21 pontos detectados em cada mão.
HAND_CONNECTIONS = (
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (5, 9), (9, 10), (10, 11), (11, 12),
    (9, 13), (13, 14), (14, 15), (15, 16),
    (13, 17), (0, 17), (17, 18), (18, 19), (19, 20),
)


def get_model_path():
    """Baixa o modelo oficial na primeira execução, se necessário."""
    if not MODEL_PATH.exists():
        print("Baixando o modelo Hand Landmarker (necessário na primeira execução)...")
        try:
            urlretrieve(MODEL_URL, MODEL_PATH)
        except Exception as exc:
            MODEL_PATH.unlink(missing_ok=True)
            raise RuntimeError(
                "Não foi possível baixar o modelo. Verifique sua conexão com a "
                f"internet e tente novamente. URL: {MODEL_URL}"
            ) from exc
    return str(MODEL_PATH)


def draw_hands(frame, hand_landmarks):
    height, width = frame.shape[:2]
    points = []

    for landmark in hand_landmarks:
        x = min(max(int(landmark.x * width), 0), width - 1)
        y = min(max(int(landmark.y * height), 0), height - 1)
        points.append((x, y))

    for start, end in HAND_CONNECTIONS:
        cv2.line(frame, points[start], points[end], (0, 255, 0), 2)

    for point in points:
        cv2.circle(frame, point, 4, (0, 0, 255), -1)


    # Usa o centro dos pontos da mão para decidir de que lado da linha está.
    hand_center_x = sum(x for x, _ in points) // len(points)
    side = "esquerda" if hand_center_x < width // 2 else "direita"
    index_raised = is_index_finger_raised(hand_landmarks)
    middle = middlefinger(hand_landmarks)
    middle_text = "Dedo medio levantado" if middle else "Dedo medio abaixado"
    index_text = "Indicador levantado" if index_raised else "Indicador abaixado"

    cv2.putText(
        frame,
        f"Mao a {side} - {index_text}",
        (max(hand_center_x - 70, 10), max(points[0][1] - 20, 30)),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2,
    )
    return middle


def is_index_finger_raised(hand_landmarks):
    """Retorna True quando a ponta do indicador está acima da articulação 6."""
    index_tip = hand_landmarks[8]
    index_middle_joint = hand_landmarks[6]
    return index_tip.y < index_middle_joint.y

def middlefinger(hand_landmarks):
    """Retorna True apenas se o dedo médio estiver levantado e os outros abaixados."""
    def finger_is_up(tip_index, joint_index):
        return hand_landmarks[tip_index].y < hand_landmarks[joint_index].y

    middle_is_up = finger_is_up(12, 10)
    index_is_up = finger_is_up(8, 6)
    ring_is_up = finger_is_up(16, 14)
    pinky_is_up = finger_is_up(20, 18)

    return middle_is_up and not (index_is_up or ring_is_up or pinky_is_up)

def main():
    BaseOptions = mp.tasks.BaseOptions
    HandLandmarker = mp.tasks.vision.HandLandmarker
    HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
    RunningMode = mp.tasks.vision.RunningMode

    options = HandLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=get_model_path()),
        running_mode=RunningMode.VIDEO,
        num_hands=2,
        min_hand_detection_confidence=0.5,
        min_hand_presence_confidence=0.5,
        min_tracking_confidence=0.5,
    )

    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise RuntimeError("Não foi possível abrir a webcam (índice 0).")

    img = None
    middle_finger_was_raised = False

    try:
        with HandLandmarker.create_from_options(options) as landmarker:
            start_time = cv2.getTickCount()
            while True:

                success, frame = camera.read()
                if not success:
                    print("Não foi possível ler um frame da webcam.")
                    break

                # Espelha a imagem para que o movimento acompanhe a mão na tela.
                width = int(camera.get(3))
                height = int(camera.get(4))

                frame = cv2.flip(frame, 1)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

                frame = cv2.line(frame, (width//2,0), (width//2, height), (0, 0, 255), 2)

                timestamp_ms = int(
                    (cv2.getTickCount() - start_time) * 1000 / cv2.getTickFrequency()
                )

                result = landmarker.detect_for_video(image, timestamp_ms)
                height, width = frame.shape[:2]
                cv2.line(
                    frame,
                    (width // 2, 0),
                    (width // 2, height),
                    (255, 0, 0),
                    2,
                )
                middle_finger_raised = False
                for hand_landmarks in result.hand_landmarks:

                    middle_finger_raised = (
                        draw_hands(frame, hand_landmarks) or middle_finger_raised
                    )

                # Sorteia uma imagem uma vez por gesto, quando o dedo é levantado.
                if middle_finger_raised and not middle_finger_was_raised:
                    fart.play()
                    Rimg = random.choice(arrayPath)
                    image_path = Path(__file__).with_name(Rimg)
                    img = cv2.imread(str(image_path))
                    if img is None:
                        raise FileNotFoundError(f"Não foi possível carregar a imagem: {image_path}")

                display_frame = frame
                if middle_finger_raised and img is not None:
                    img_width = int(img.shape[1] * height / img.shape[0])
                    resized_img = cv2.resize(img, (img_width, height))
                    display_frame = np.hstack((frame, resized_img))

                cv2.imshow("Rastreamento de mãos - pressione Q para sair", display_frame)
                middle_finger_was_raised = middle_finger_raised
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
