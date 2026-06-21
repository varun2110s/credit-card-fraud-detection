import streamlit as st
import joblib
import numpy as np
import shap
import matplotlib.pyplot as plt

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

        # SHAP explanation
        st.write('### Why this prediction?')
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(features)
        fig, ax = plt.subplots()
        shap.waterfall_plot(shap.Explanation(
            values=shap_values[0][0],
            base_values=explainer.expected_value[0],
            data=features[0]))
        st.pyplot(fig)

    except Exception as e:
        st.warning(f'Error: {e}')