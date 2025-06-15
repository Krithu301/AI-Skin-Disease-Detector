from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model
model = load_model("model.h5")

# Disease class names
class_names = ["Acne", "Eczema", "Psoriasis", "Rosacea", "Melanoma", "Ringworm", "Vitiligo"]

# Get model input shape dynamically
input_shape = model.input_shape[1:]  # e.g. (180, 180, 3)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files.get('image')
    
    if not file:
        return render_template("index.html", prediction="⚠ Please upload an image.")

    try:
        # Process the image
        img = Image.open(file).convert("RGB")
        img = img.resize((input_shape[0], input_shape[1]))
        img_array = np.array(img).reshape(1, *input_shape)
        img_array = img_array / 255.0  # Normalize

        # Make prediction
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction)
        result = class_names[predicted_class]

        return render_template("index.html", prediction=f"🌟 Predicted Disease: {result}")
    
    except Exception as e:
        return render_template("index.html", prediction=f"❌ Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)