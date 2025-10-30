# ML utility functions for loading model and making predictions
import joblib
import os
import numpy as np

# Global variables to store loaded model and preprocessor
model = None
preprocessor = None

def load_ml_components():
    """Load the ML model and preprocessor"""
    global model, preprocessor
    model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'trained_model.pkl')
    preprocessor_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'preprocessor.pkl')
    
    model = joblib.load(model_path)
    preprocessor = joblib.load(preprocessor_path)
    print("ML components loaded successfully!")

def predict(input_data):
    """Make prediction using loaded model"""
    if model is None or preprocessor is None:
        raise ValueError("ML components not loaded. Call load_ml_components() first.")
    
    # Preprocess input
    input_array = np.array([list(input_data.dict().values())])
    input_scaled = preprocessor.transform(input_array)
    
    # Make prediction
    prediction = model.predict(input_scaled)[0]
    probabilities = model.predict_proba(input_scaled)[0]
    confidence = max(probabilities)
    
    # Map prediction to class name
    class_names = {0: "Not a real planet", 1: "Possible Planet", 2: "Confirmed Planet"}
    
    return {
        "prediction": int(prediction),
        "confidence": float(confidence),
        "class_name": class_names[prediction]
    }