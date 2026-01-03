import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import os

# ---------------------- Setup ----------------------

# Title of the app
st.set_page_config(page_title="Animal Classifier", layout="centered")
st.title("🦁 Real-Time Animal Image Classification")
st.markdown("This app uses your webcam to classify animals using a pre-trained deep learning model.")

# ---------------------- Load Model ----------------------

MODEL_PATH = "model.h5"  # Make sure model.h5 is in the same folder
DATASET_DIR = "dataset/train"  # Change this path to your dataset's train folder

try:
    model = load_model(MODEL_PATH)
    class_names = sorted(os.listdir(DATASET_DIR))
    st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# ---------------------- Functions ----------------------

def preprocess_frame(frame):
    """Resize and normalize image for prediction"""
    img = cv2.resize(frame, (224, 224))  # Assumes MobileNetV2 input
    img = img / 255.0
    return np.expand_dims(img, axis=0)

def predict(frame):
    """Run prediction on the frame"""
    processed = preprocess_frame(frame)
    prediction = model.predict(processed)
    class_idx = np.argmax(prediction)
    confidence = float(prediction[0][class_idx])
    label = class_names[class_idx]
    return label, confidence

# ---------------------- Streamlit Webcam UI ----------------------

run = st.checkbox('📸 Start Webcam')

FRAME_WINDOW = st.image([])

if run:
    cap = cv2.VideoCapture(0)
    st.info("Press 'Q' in webcam window to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            st.warning("Failed to grab frame.")
            break

        frame = cv2.flip(frame, 1)  # Mirror image
        label, confidence = predict(frame)

        # Display prediction on frame
        text = f"{label} ({confidence*100:.2f}%)"
        cv2.putText(frame, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
else:
    st.write("🛑 Webcam is off. Check the box to turn it on.")

