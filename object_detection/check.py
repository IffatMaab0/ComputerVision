from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model("images/crowd.jpg", iou=0.5, show=True)

result = results[0]


