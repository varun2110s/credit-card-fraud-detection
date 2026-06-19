import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load('fraud_detection_model.pkl')

st.title('💳 Credit Card Fraud Detection')
st.write('Enter transaction features to check if it is fraud or normal.')

# Input field
features_input = st.text_area('Enter 30 features (comma separated)')

# Predict button
if st.button('Check Transaction'):
    try:
        features = np.array(features_input.split(','), dtype=float).reshape(1, -1)
        prediction = model.predict(features)
        if prediction[0] == 1:
            st.error('🚨 FRAUD Transaction Detected!')
        else:
            st.success('✅ Normal Transaction')
    except:
        st.warning('Please enter valid features!')
