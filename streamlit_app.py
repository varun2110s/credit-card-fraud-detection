import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load('fraud_detection_model.pkl')

st.title('💳 Credit Card Fraud Detection')
st.write('Enter transaction details to check if it is fraud or normal.')

# User friendly inputs
amount = st.number_input('Transaction Amount (₹)', min_value=0.0, max_value=50000.0, value=100.0)
time = st.number_input('Time (seconds since first transaction)', min_value=0.0, max_value=200000.0, value=50000.0)

if st.button('Check Transaction'):
    v_features = [0.0] * 28
    amount_scaled = (amount - 88.35) / 250.12
    time_scaled = (time - 94813.86) / 47488.15
    features = np.array(v_features + [amount_scaled, time_scaled]).reshape(1, -1)
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.error('🚨 FRAUD Transaction Detected!')
    else:
        st.success('✅ Normal Transaction')