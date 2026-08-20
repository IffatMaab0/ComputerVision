import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

cap = cv2.VideoCapture("videos/vid.mp4")

car_ids = set()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model.track(
        frame,
        persist=True
    )

    result = results[0]

    if result.boxes.id is not None:

        track_ids = result.boxes.id.int().cpu().tolist()

        for box, track_id in zip(
            result.boxes,
            track_ids
        ):

            class_id = int(box.cls[0])
            class_name = model.names[class_id]

            if class_name == "car":
                car_ids.add(track_id)

    annotated_frame = result.plot()

    cv2.putText(
        annotated_frame,
        f"Cars seen: {len(car_ids)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow(
        "Car Tracking",
        annotated_frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()