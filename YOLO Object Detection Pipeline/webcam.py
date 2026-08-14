import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

cap = cv2.VideoCapture("videos/vid.mp4")

while True:

    ret, frame = cap.read()

    if not ret:
        print("Video finished")
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Video Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()