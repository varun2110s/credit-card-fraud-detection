import streamlit as st
import joblib
import numpy as np
import shap
import pandas as pd

# Load the saved model
model = joblib.load('fraud_detection_model.pkl')

st.title('💳 Credit Card Fraud Detection')
st.write('Enter transaction features to check if it is fraud or normal.')

# Input field
features_input = st.text_area('Enter 30 features (comma separated)')

if st.button('Check Transaction'):
    try:
        features = np.array(features_input.split(','), dtype=float).reshape(1, -1)
        prediction = model.predict(features)
        probability = model.predict_proba(features)[0]

        if prediction[0] == 1:
            st.error('🚨 FRAUD Transaction Detected!')
            st.write(f'**Confidence:** {round(probability[1] * 100, 2)}% chance of fraud')
            st.write('---')
            st.write('### Why is this transaction suspicious?')

            # SHAP
            feature_names = [f'V{i}' for i in range(1, 29)] + ['Amount_scaled', 'Time_scaled']
            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(features)
            importance = pd.Series(shap_values[0, :, 1], index=feature_names)
            top_features = importance.abs().nlargest(3)

            st.write('The following unusual patterns were detected in this transaction:')
            for i, feature in enumerate(top_features.index, 1):
                st.write(f'**{i}.** Unusual activity detected in transaction pattern **{feature}**')

            st.write('---')
            st.write('⚠️ This transaction has been flagged for review.')

        else:
            st.success('✅ Normal Transaction')
            st.write(f'**Confidence:** {round(probability[0] * 100, 2)}% chance of being normal')
            st.write('This transaction appears to be safe.')

    except Exception as e:
        st.warning(f'Error: {e}')