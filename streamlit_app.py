
import streamlit as st
import numpy as np
from PIL import Image
from ultralytics import YOLO

# Page configuration
st.set_page_config(
    page_title="Pothole & Defect Detector",
    page_icon="🚧",
    layout="wide"
)

st.title("🚧 AI-Based Pothole & Defect Detector")
st.write("Upload a road image to detect potholes and estimate road severity.")

# Load trained YOLO model
@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

# Severity calculation
def calculate_severity(coverage):
    if coverage == 0:
        return "NONE"
    elif coverage <= 3:
        return "LOW"
    elif coverage <= 10:
        return "MEDIUM"
    elif coverage <= 20:
        return "HIGH"
    else:
        return "CRITICAL"

# Image upload
uploaded_file = st.file_uploader(
    "Upload a road image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.subheader("Uploaded Image")
    st.image(image, use_container_width=True)

    if st.button("Detect Potholes"):

        with st.spinner("Detecting potholes..."):
            results = model.predict(image, conf=0.25, verbose=False)
            result = results[0]

            image_area = result.orig_shape[0] * result.orig_shape[1]
            total_box_area = 0

            detections = []

            if result.boxes is not None:
                for box in result.boxes:
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()

                    box_area = max(0, x2 - x1) * max(0, y2 - y1)
                    total_box_area += box_area

                    confidence = float(box.conf[0].cpu().numpy())

                    detections.append(confidence)

            coverage = (total_box_area / image_area) * 100
            severity = calculate_severity(coverage)

            annotated_image = result.plot()[:, :, ::-1]

        st.subheader("Detection Results")

        col1, col2 = st.columns(2)

        with col1:
            st.image(
                annotated_image,
                caption="Detected Potholes",
                use_container_width=True
            )

        with col2:
            st.metric("Detected Potholes", len(detections))
            st.metric("Defect Coverage", f"{coverage:.2f}%")
            st.metric("Road Severity", severity)

            if detections:
                st.write("**Confidence Scores:**")
                for i, confidence in enumerate(detections, start=1):
                    st.write(f"Pothole {i}: {confidence * 100:.2f}%")
            else:
                st.info("No potholes detected in this image.")
