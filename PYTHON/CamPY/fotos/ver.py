import cv2
from facial_recognition import recognize_image

webcam = cv2.VideoCapture(0)

while True:
    quadros = webcam.read()
    lag = webcam.read()

    if not lag:
        break

    resultSet = recognize_image(
        quadros, save_output=False
    )

    for pessoa in resultSet:
        nomePessoa = pessoa["name"]

        x,y,a,l = pessoa["box"]

        altura, largura = quadros.shape[:2]

        x1 = int(x * largura)
        y1 = int(y * altura)
        x2 = int(x + l * largura)
        y2 = int(y + a * altura)

        cv2.rectangle(
            quadros, (x1,y1), (x2,y2), (255,0,0), 2
        )

        cv2.putText(
            quadros, nomePessoa, (x1, y1 - 15), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,0,0), 2
        )

cv2.imshow("Reconhecimento Facial com Python", quadros)

