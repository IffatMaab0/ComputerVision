import cv2
import time
from ultralytics import YOLO

model = YOLO("yolo11m.pt")

cap = cv2.VideoCapture("videos/vid.mp4")

while True:

    start_time = time.time()

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    end_time = time.time()

    fps = 1 / (end_time - start_time)

    cv2.putText(
        annotated_frame,
        f"FPS: {fps:.2f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("YOLO Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()