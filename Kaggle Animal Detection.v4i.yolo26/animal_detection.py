from ultralytics import YOLO
import cv2

# Load trained model
model = YOLO("runs/detect/train/weights/best.pt")

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Run detection
    results = model(frame, conf=0.5)

    # Draw bounding boxes
    annotated_frame = results[0].plot()

    # Show frame
    cv2.imshow("Animal Detection", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
