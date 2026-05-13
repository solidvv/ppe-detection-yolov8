from ultralytics import YOLO
import os

model = YOLO('weights/best.pt')

results = model.predict(
    source='datasets/test/images', 
    save=True,      
    conf=0.5,       
    line_width=2,
    project='runs/detect',
    name='predict',
    exist_ok=True
)

print("---")
print("Results are here: runs/detect/predict")