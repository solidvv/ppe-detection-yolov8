# PPE Detection using YOLOv8

This repository contains a YOLOv8-based system for detecting Personal Protective Equipment (PPE) such as hard hats and safety vests. The project is containerized using Docker for easy deployment and reproduction.

## Performance
- **Model:** YOLOv8n
- **Speed:** ~12.5 FPS (tested on NVIDIA 2060 SUPER GPU)
- **Status:** Initial version (v1.0)

## Project Structure
- `weights/` - Pre-trained model weights (`best.pt`).
- `datasets/` - Directory for training/testing data (not included in repo).
- `prediction.py` - Script for running inference on test images.
- `train.py` - Script for training the model.
- `split.py` - Utility to split a single `train` folder into `train/valid/test`.

## Setup & Usage

### 1. Requirements
- Docker & Docker Compose
- NVIDIA Container Toolkit (for GPU support)

### 2. Dataset
You can find the dataset used for this project here: https://universe.roboflow.com/kust-frp58/personal-protective-equipment-2dlgs 
Place your data in the `datasets/` folder following the standard YOLO structure.

### 3. Data Splitting (Optional)
If your dataset only contains a `train` folder, run the following command to split it (80/20/10 ratio):
```bash
docker compose run yolo-worker python split.py
```
### 4. Running Inference

To process images in datasets/test/images and save results to runs/detect/predict:
```Bash

docker compose up
```
### 5. Training

To start a new training session:
```Bash

docker compose run yolo-worker python train.py
```