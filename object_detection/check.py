from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model("images/3things.webp")

result = results[0]

for box in result.boxes:

    class_id = int(box.cls[0])
    confidence = float(box.conf[0])

    class_name = model.names[class_id]

    print(
        f"Object: {class_name} | "
        f"Confidence: {confidence:.2f}"
    )


result.save(filename="outputs/result3things.jpg")