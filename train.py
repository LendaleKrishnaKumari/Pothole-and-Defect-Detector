
from ultralytics import YOLO
import argparse

def train_model(data_yaml):
    # Load pretrained YOLOv8 Nano model
    model = YOLO("yolov8n.pt")

    # Train on the pothole dataset
    results = model.train(
        data=data_yaml,
        epochs=50,
        imgsz=640,
        batch=16,
        device=0,
        workers=2,
        patience=10,
        freeze=10,
        project="Pothole_Project",
        name="YOLOv8_Pothole_Training",
        exist_ok=True,
        plots=True,
        save=True
    )

    print("Training completed!")
    print("Best model: Pothole_Project/YOLOv8_Pothole_Training/weights/best.pt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train YOLOv8 for pothole detection"
    )

    parser.add_argument(
        "--data",
        required=True,
        help="Path to the YOLO dataset data.yaml file"
    )

    args = parser.parse_args()
    train_model(args.data)
