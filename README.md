# AI-Based Pothole & Defect Detector

## Project Overview
An AI-based road defect detection application using YOLOv8.

## Features
- Pothole detection using YOLOv8
- Bounding boxes around detected potholes
- Confidence scores
- Defect coverage percentage
- Road severity classification
- Interactive Streamlit web application

## Severity Classification
| Defect Coverage | Severity |
|---|---|
| No detection | NONE |
| Up to 3% | LOW |
| Above 3% to 10% | MEDIUM |
| Above 10% to 20% | HIGH |
| Above 20% | CRITICAL |

## Run Locally
Install dependencies: pip install -r requirements.txt
Run application: streamlit run streamlit_app.py

## Model
YOLOv8n fine-tuned on the Pothole-VoxRL dataset.
Evaluation metrics will be added using actual test results.

## Limitations
Performance may vary depending on image quality, lighting,
road conditions, and pothole size.