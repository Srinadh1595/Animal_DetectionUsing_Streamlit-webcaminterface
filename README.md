# 🐾 Real-Time Animal Classification System

A deep learning-powered web application that classifies animal species from images or live webcam feeds using transfer learning with MobileNetV2. Built with TensorFlow, Keras, and Streamlit.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.19.0-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📋 Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Dataset](#dataset)
- [Training](#training)
- [Performance](#performance)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- 🎥 **Real-time Webcam Classification**: Classify animals using your webcam in real-time
- 📤 **Image Upload Support**: Upload JPG, JPEG, or PNG images for classification
- 🎯 **Top-3 Predictions**: View the top 3 most likely animal classifications with confidence scores
- 🌐 **Interactive Web Interface**: User-friendly Streamlit-based UI with intuitive design
- 🚀 **Optimized Model**: Lightweight model (~11MB) for fast inference
- 📊 **Confidence Scores**: Detailed confidence percentages for each prediction
- 🎨 **Modern UI**: Clean and responsive interface with visual feedback

## 🎬 Demo

The application supports two input modes:

1. **Webcam Mode**: Take a photo using your device's camera
2. **Upload Mode**: Upload an image file from your computer

Both modes provide instant classification results with confidence scores and top-3 predictions.

## 🛠 Technologies Used

### Core Framework
- **Python 3.x**: Primary programming language
- **TensorFlow 2.19.0**: Deep learning framework
- **Keras**: High-level neural network API

### Machine Learning
- **MobileNetV2**: Pre-trained CNN architecture for transfer learning
- **Transfer Learning**: Fine-tuned on custom animal dataset
- **Data Augmentation**: Rotation, zoom, shifts for robust training

### Web Framework & UI
- **Streamlit**: Web application framework for interactive UI
- **OpenCV**: Computer vision and image processing
- **NumPy**: Numerical computing and array operations
- **Pillow**: Image processing and file handling

## 📁 Project Structure

```
project/
├── app.py                      # Main Streamlit application
├── model.h5                    # Trained model file (needs to be trained first)
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── train_model.py/             # Model training scripts
│   ├── train.py               # Training script
│   └── app.py                 # Alternative app version
├── animaldaset/                # Training dataset directory
│   └── train/                 # Training images organized by class
│       ├── cat/
│       ├── dog/
│       ├── bird/
│       └── ...
├── setup_tensorflow.py         # Environment setup script
├── reorganize_dataset.py       # Dataset organization utility
└── project_overview.md         # Additional project documentation
```

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Git (optional, for cloning the repository)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/animal-classification.git
cd animal-classification
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv tf_env

# Activate virtual environment
# On Windows:
tf_env\Scripts\activate
# On macOS/Linux:
source tf_env/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Prepare the Model

You have two options:

**Option A: Use Pre-trained Model**
- Place your trained `model.h5` file in the root directory

**Option B: Train Your Own Model**
- Organize your dataset in `animaldaset/train/` with class folders
- Run the training script:
```bash
python train_model.py/train.py
```

## 💻 Usage

### Running the Application

1. Make sure your virtual environment is activated
2. Ensure `model.h5` exists in the root directory
3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Open your browser and navigate to the URL shown (typically `http://localhost:8501`)

### Using the Application

1. **Webcam Mode**:
   - Click on the "📸 Webcam" tab
   - Allow camera permissions when prompted
   - Click "Take a picture" to capture an image
   - View the classification results instantly

2. **Upload Mode**:
   - Click on the "📤 Upload Image" tab
   - Click "Browse files" and select an image (JPG, JPEG, or PNG)
   - The image will be automatically classified
   - View the predicted animal class and confidence scores

## 🧠 Model Details

### Architecture

- **Base Model**: MobileNetV2 (pre-trained on ImageNet)
- **Input Size**: 224×224×3 pixels
- **Transfer Learning**: Frozen base layers with custom classification head
- **Custom Layers**:
  - GlobalAveragePooling2D
  - Dropout (0.3)
  - Dense (128 units, ReLU activation)
  - Dense (num_classes, Softmax activation)

### Training Configuration

- **Optimizer**: Adam (learning rate: 0.0001)
- **Loss Function**: Categorical Crossentropy
- **Metrics**: Accuracy
- **Batch Size**: 32
- **Epochs**: 10 (configurable)
- **Data Split**: 80% training, 20% validation
- **Data Augmentation**:
  - Rotation: ±15°
  - Zoom: 0.2
  - Width/Height Shift: 0.1
  - Horizontal Flip: Yes

## 📊 Dataset

The model is trained on a custom animal dataset containing multiple animal species. The dataset should be organized as follows:

```
animaldaset/
└── train/
    ├── antelope/
    ├── badger/
    ├── bat/
    ├── bear/
    ├── cat/
    ├── dog/
    └── ... (more animal classes)
```

Each class folder should contain training images (JPG format recommended).

**Note**: The dataset is not included in this repository due to size constraints. You'll need to organize your own dataset or use a publicly available animal dataset.

## 🎓 Training

To train the model on your own dataset:

1. Organize your dataset in the `animaldaset/train/` directory
2. Update the `DATASET_DIR` path in `train_model.py/train.py` if needed
3. Run the training script:

```bash
python train_model.py/train.py
```

4. The trained model will be saved as `model.h5` in the root directory
5. Monitor training progress through accuracy and loss metrics

## ⚡ Performance

- **Model Size**: ~11MB (optimized for deployment)
- **Inference Time**: Real-time processing (< 1 second per image)
- **Supported Image Formats**: JPG, JPEG, PNG
- **Supported Classes**: Depends on your training dataset

**Note**: Model accuracy depends on:
- Dataset quality and size
- Number of training epochs
- Data augmentation techniques
- Image quality and clarity

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is done by srinadh

## 🙏 Acknowledgments

- MobileNetV2 architecture by Google
- TensorFlow and Keras teams for the excellent deep learning framework
- Streamlit for the amazing web app framework
- All contributors and open-source community

## 📧 Contact

Mail:srinadherakala1595@gmail.com.

---

