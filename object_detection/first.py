from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model("images/cat.webp")
results[0].show()