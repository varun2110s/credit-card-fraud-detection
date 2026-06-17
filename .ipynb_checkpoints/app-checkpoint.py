from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the saved model
model = joblib.load('fraud_detection_model.pkl')

# Home route - check if API is running
@app.route('/')
def home():
    return "Fraud Detection API is running!"

# Predict route - takes transaction data and returns fraud prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    result = 'Fraud' if prediction[0] == 1 else 'Normal'
    return jsonify({'prediction': result})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)