import streamlit as st
import joblib
import numpy as np
import shap
import pandas as pd

# Load the saved model
model = joblib.load('fraud_detection_model.pkl')

st.title('💳 Credit Card Fraud Detection')
st.write('Select a transaction to check if it is fraud or normal.')

# Predefined transactions
fraud_values = [-2.312226542, 1.951992011, -1.609850732, 3.997905588, -0.522187865, -1.426545319, -2.537387306, 1.391657248, -2.770089277, -2.772272145, 3.202033207, -2.899907388, -0.595221881, -4.289253782, 0.38972412, -1.14074718, -2.830055675, -0.016822468, 0.416955705, 0.126910559, 0.517232371, -0.035049369, -0.465211076, 0.320198199, 0.044519167, 0.177839798, 0.261145003, -0.143275875, -0.35322939296682354, -1.9880335064229064]

normal_values = [1.191857, 0.266151, 0.166480, 0.448154, 0.060018, -0.082361, -0.078803, 0.085102, -0.255425, -0.166974, 1.612727, 1.065235, 0.489095, -0.143772, 0.635558, 0.463917, -0.114805, -0.183361, -0.145783, -0.069083, -0.225775, -0.638672, 0.101288, -0.339846, 0.167170, 0.125895, -0.008983, 0.014724, -0.342475, -1.996583]

option = st.selectbox('Choose a transaction to test:', [
    'Select...',
    '🔴 Test Fraud Transaction',
    '🟢 Test Normal Transaction'
])

if st.button('Check Transaction'):
    if option == 'Select...':
        st.warning('Please select a transaction first!')
    else:
        features = np.array(fraud_values if 'Fraud' in option else normal_values).reshape(1, -1)
        prediction = model.predict(features)
        probability = model.predict_proba(features)[0]

        if prediction[0] == 1:
            st.error('🚨 FRAUD Transaction Detected!')
            st.write(f'**Confidence:** {round(probability[1] * 100, 2)}% chance of fraud')
            st.write('---')
            st.write('### Why is this transaction suspicious?')
            feature_names = [f'V{i}' for i in range(1, 29)] + ['Amount_scaled', 'Time_scaled']
            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(features)
            importance = pd.Series(shap_values[0, :, 1], index=feature_names)
            top_features = importance.abs().nlargest(3)
            st.write('The following unusual patterns were detected:')
            for i, feature in enumerate(top_features.index, 1):
                st.write(f'**{i}.** Unusual activity detected in transaction pattern **{feature}**')
            st.write('---')
            st.write('⚠️ This transaction has been flagged for review.')
        else:
            st.success('✅ Normal Transaction')
            st.write(f'**Confidence:** {round(probability[0] * 100, 2)}% chance of being normal')
            st.write('This transaction appears to be safe.')