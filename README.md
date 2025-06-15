# 🌟 AI-Based Skin Disease Detection System

This project is a deep learning-based web application that allows users to upload images of skin conditions and get predictions about possible skin diseases.

## 📌 Key Features

- 🔍 Predicts skin diseases from uploaded images
- 🤖 Powered by a trained deep learning model (TensorFlow/Keras)
- 🧠 Convolutional Neural Networks (CNN) for image classification
- 🌐 Flask-based web interface
- 📊 Clean and colorful user interface

---

## 🧰 Tech Stack

- Python 3.x
- TensorFlow / Keras
- NumPy
- Flask
- HTML / CSS (Frontend)

---

## 🗂 Dataset

The model was trained on a skin disease image dataset containing multiple classes of common skin conditions. Due to size limitations, the dataset is not uploaded here.

---

## 📁 Model File

The trained model file (model.h5) can be downloaded from this [Google Drive link](https://drive.google.com/file/d/1L3469RZl6KtwnEojj0Dvjx-UAo54MykF/view?usp=sharing).  
Place it in the same directory as app.py before running.

---

## 💻 How to Run Locally

# Step 1: Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

# Step 2: Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate     # On Windows
# OR
source venv/bin/activate  # On Mac/Linux

# Step 3: Install required packages
pip install -r requirements.txt

# Step 4: Download model.h5 from the link above and place it in the same folder

# Step 5: Run the app
python app.py

---

Open your browser and go to:
👉 http://127.0.0.1:5000
