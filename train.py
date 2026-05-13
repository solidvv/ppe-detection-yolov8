from ultralytics import YOLO

def main():
    model = YOLO('yolov8n.pt')

    model.train(
        data='datasets/data.yaml', 
        epochs=50, 
        imgsz=640, 
        device=0, 
        workers=4
    )

if __name__ == '__main__':
    main()