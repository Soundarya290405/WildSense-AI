from ultralytics import YOLO
import cv2
import requests

model = YOLO("runs/detect/train/weights/best.pt")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            name = model.names[cls]

            print("Detected:", name)

            # send data to backend
            requests.post(
                "http://10.239.216.195:5000/detect",
                json={
                    "animal": name,
                    "location": "Farm Camera 1"
                }
            )

    annotated_frame = results[0].plot()

    cv2.imshow("Animal Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()