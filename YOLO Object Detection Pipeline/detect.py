from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model("images/test.jpg")

result = results[0]

print("Image shape:")
print(result.orig_shape)

print("\nBoxes:")
print(result.boxes)

print("\nCoordinates:")
print(result.boxes.xyxy)

print("\nConfidence:")
print(result.boxes.conf)

print("\nClass IDs:")
print(result.boxes.cls)

print("\nClass names:")
print(model.names)