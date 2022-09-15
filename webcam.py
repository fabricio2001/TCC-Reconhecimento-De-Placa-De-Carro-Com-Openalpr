import cv2
from openalpr import Alpr
import numpy as np

alpr = Alpr("br", "openalpr.conf","runtime_data")

if not alpr.is_loaded():
    print("Error loading openalpr")
    sys.exit(1)

alpr.set_top_n(20)
alpr.set_default_region("br")

cap = cv2.VideoCapture("resource/videos/1.mp4")

while True:
    placa = np.ones((100, 400, 3)) * 255

    ret, img = cap.read()

    img_str = cv2.imencode('.jpg', img)[1].tostring()
    result = alpr.recognize_array(img_str)

    for plate in result["results"]:
        cv2.putText(placa, plate['plate'], (50,50), 0, 2, (255,0,0), 2)
        cv2.rectangle(img, (plate['coordinates'][0]['x'], plate['coordinates'][0]['y']), 
                            (plate['coordinates'][1]['x'], plate['coordinates'][1]['y']), (255,0,0), 2)

    cv2.imshow("img", img)
    cv2.imshow("placa", placa)

    if cv2.waitKey(1) == 27:
        break