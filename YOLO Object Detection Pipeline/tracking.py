import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

cap = cv2.VideoCapture("videos/vid.mp4")

track_positions = {}
counted_ids = set()

car_count = 0

COUNTING_LINE_X = 500

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

            if class_name != "car":
                continue

            x1, y1, x2, y2 = box.xyxy[0]

            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            # Previous position
            previous_x = track_positions.get(track_id)

            # Check whether car crossed the line
            if previous_x is not None:

                if (
                    previous_x < COUNTING_LINE_X
                    and center_x >= COUNTING_LINE_X
                    and track_id not in counted_ids
                ):

                    car_count += 1
                    counted_ids.add(track_id)

            # Update position
            track_positions[track_id] = center_x

            # Draw center point
            cv2.circle(
                result.orig_img,
                (center_x, center_y),
                5,
                (0, 0, 255),
                2
            )

    # Draw counting line
    cv2.line(
        result.orig_img,
        (COUNTING_LINE_X, 0),
        (COUNTING_LINE_X, frame.shape[0]),
        (255, 0, 0),
        2
    )

    # Display count
    cv2.putText(
        result.orig_img,
        f"Cars crossed: {car_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow(
        "Traffic Counter",
        result.orig_img
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()