from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model("images/3things.webp" , conf=0.4, iou=0.7)

result = results[0]
result.show()
for box in result.boxes:

    x1, y1, x2, y2 = box.xyxy[0]

    class_id = int(box.cls[0])
    confidence = float(box.conf[0])

    print("Class:", model.names[class_id])
    print("Confidence:", confidence)

    print("x1:", float(x1))
    print("y1:", float(y1))
    print("x2:", float(x2))
    print("y2:", float(y2))

    print("----------------")