from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model("images/cat.webp")
result = results[0]
# print('Boxes')
# print(result.boxes.xyxy)
# print('Confidences')
# print(result.boxes.conf)
# print('Classes')
# print(result.boxes.cls)
for box in result.boxes:

    class_id = int(box.cls[0])
    confidence = float(box.conf[0])

    class_name = model.names[class_id]

    print(class_name, confidence)