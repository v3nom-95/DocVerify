# 🛡️ DocVerify - Advanced Document Verification System

![DocVerify Hero](hero.png)

## 📋 Table of Contents
- [Overview](#-overview)
- [Tech Stack](#-tech-stack)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Getting Started](#-getting-started)
- [Usage](#-usage)
- [Troubleshooting](#-troubleshooting)
- [Contributors](#-contributors)

---

## 🌟 Overview

**DocVerify** is a high-performance, AI-driven document verification system specifically designed for validating identity documents like Aadhar cards. Leveraging the power of **YOLOv8** (You Only Look Once), the system performs real-time object detection to identify and verify critical security features, ensuring document authenticity and completeness.

Developed as a modern web application, DocVerify provides an intuitive interface for users to upload documents and receive detailed verification reports within seconds.

---

## 💻 Tech Stack

| Category | Technologies |
| :--- | :--- |
| **Backend** | ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| **AI / Machine Learning** | ![YOLOv8](https://img.shields.io/badge/YOLOv8-00FFFF?style=for-the-badge&logo=ultralytics&logoColor=black) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white) ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white) |
| **Frontend** | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) |
| **Visualization** | ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white) ![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge) |

---

## 🚀 Key Features

- 🤖 **AI-Powered Detection**: Deep learning models trained on thousands of document samples.
- ⚡ **Real-Time Verification**: Instant analysis of document elements.
- 🔍 **Granular Validation**: Checks for 8+ specific elements (QR Code, Name, Photo, etc.).
- 📊 **Detailed Reporting**: Visual feedback on detected and missing elements.
- 🎨 **Modern UI**: Sleek, responsive interface with drag-and-drop support.
- 📈 **Performance Metrics**: Included scripts for training and validation analysis.

---

## 🏗️ System Architecture

```mermaid
graph TD
    A[User Uploads Image] --> B[Flask Backend]
    B --> C[Image Preprocessing - OpenCV]
    C --> D[YOLOv8 Inference]
    D --> E{Element Analysis}
    E -->|All Found| F[Verified ✔️]
    E -->|Elements Missing| G[Not Verified ❌]
    F --> H[JSON Response]
    G --> H[JSON Response]
    H --> I[Frontend Display]
```

---

## 🛠️ Getting Started

### Prerequisites
- Python 3.8 or higher
- Pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/v3nom-95/doc-verification.git
   cd doc-verification
   ```

2. **Set up Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install flask opencv-python ultralytics torch matplotlib seaborn pandas
   ```

---

## 📲 Usage

1. **Start the Application**
   ```bash
   python app.py
   ```

2. **Access the Portal**
   Open your browser and navigate to `http://127.0.0.1:5000`

3. **Verify Document**
   - Click "Choose File" or Drag & Drop an image.
   - Wait for the AI to process and display the results.

---

## 🔧 Troubleshooting

### ⚠️ Common Issues

- **500 Internal Server Error**: This usually occurs if the AI model file is missing. Ensure the model exists at:
  `New folder/ps/adharmodel/best2.pt`
- **Invalid File Type**: Ensure you are uploading only `.jpg`, `.jpeg`, or `.png` files.
- **Low Confidence Scores**: Ensure the document is well-lit and the image quality is high for better detection.

---


<p align="center">Made with ❤️ for Academic Excellence</p>
