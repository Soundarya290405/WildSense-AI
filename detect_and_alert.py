from ultralytics import YOLO
import cv2
import requests

model = YOLO("runs/detect/train/weights/best.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    results = model(frame)

    for r in results:
        if len(r.boxes) > 0:
            print("Animal Detected!")

            # send alert to server
            try:
                requests.get("http://10.239.216.195:5000/animal")
            except:
                pass

    frame = results[0].plot()

    cv2.imshow("Animal Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()