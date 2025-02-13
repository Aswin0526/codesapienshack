from ultralytics import YOLO

model = YOLO('best.pt')

results = model(source = 'rust.jpg',conf=0.4, save=True)