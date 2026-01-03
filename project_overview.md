# Animal Classification Project

## Project Overview
A real-time animal classification system that uses deep learning to identify different animal species from images or webcam feeds. The project implements transfer learning using MobileNetV2 and provides an interactive web interface for easy usage.

## Key Features
- **Real-time Classification**: Live animal detection using webcam
- **Image Upload**: Support for JPG, JPEG, PNG image uploads
- **Interactive Web Interface**: User-friendly Streamlit-based UI
- **Top-3 Predictions**: Shows confidence scores for multiple predictions
- **Model Persistence**: Trained model saved for deployment

## Technical Stack

### Frontend
- **Streamlit**: Web application framework for interactive UI
- **HTML/CSS**: Styled components and responsive design

### Backend
- **Python 3.x**: Primary programming language
- **TensorFlow 2.19.0**: Deep learning framework
- **Keras**: High-level neural network API
- **OpenCV**: Computer vision and image processing
- **NumPy**: Numerical computing and array operations
- **Pillow**: Image processing and file handling

### Machine Learning
- **MobileNetV2**: Pre-trained CNN for transfer learning
- **Transfer Learning**: Fine-tuned on custom animal dataset
- **Data Augmentation**: Rotation, zoom, shifts for robust training
- **Image Preprocessing**: Resizing, normalization, color conversion

## Project Architecture
```
User Interface (Streamlit)
    ↓
Image Processing (OpenCV/NumPy)
    ↓
Neural Network (MobileNetV2 + Custom Layers)
    ↓
Prediction Output (Animal Class + Confidence)
```

## Model Specifications
- **Input Size**: 224x224x3 pixels
- **Base Model**: MobileNetV2 (pre-trained on ImageNet)
- **Training**: Transfer learning with frozen base layers
- **Output**: Multi-class classification (animal species)
- **Optimizer**: Adam (learning rate: 0.0001)
- **Loss Function**: Categorical Crossentropy
- **Metrics**: Accuracy

## Data Pipeline
1. **Data Loading**: ImageDataGenerator with augmentation
2. **Preprocessing**: Resize, normalize, augment
3. **Training**: 80% train, 20% validation split
4. **Inference**: Real-time prediction on new images

## Performance Metrics
- **Model Size**: ~11MB (optimized for deployment)
- **Inference Time**: Real-time processing
- **Accuracy**: Varies based on dataset quality
- **Supported Formats**: JPG, JPEG, PNG

## Deployment
- **Platform**: Streamlit Cloud or local deployment
- **Dependencies**: requirements.txt for easy setup
- **Model Storage**: HDF5 format (.h5 file)
- **Environment**: Python virtual environment

## Usage Instructions
1. **Webcam Mode**: Click camera button, take photo, get instant classification
2. **Upload Mode**: Select image file, view classification results
3. **Results**: Shows predicted animal and confidence percentage
4. **Top-3**: Displays multiple predictions with confidence scores

## Project Structure
```
project/
├── app.py                 # Main Streamlit application
├── train_model.py/        # Model training scripts
├── model.h5              # Trained model file
├── requirements.txt       # Python dependencies
├── animaldaset/          # Training dataset
└── setup_tensorflow.py   # Environment setup
```

## Skills Demonstrated
- **Deep Learning**: CNN, Transfer Learning, Model Architecture
- **Computer Vision**: Image Processing, OpenCV, Data Augmentation
- **Web Development**: Streamlit, Interactive UI Design
- **Machine Learning**: Model Training, Evaluation, Deployment
- **Python Programming**: Object-Oriented Design, Data Processing
- **Software Engineering**: Project Structure, Dependency Management

## Learning Outcomes
- Implemented transfer learning with pre-trained models
- Built end-to-end ML pipeline from data to deployment
- Created interactive web interface for ML applications
- Applied computer vision techniques for image classification
- Developed production-ready ML application with user interface 