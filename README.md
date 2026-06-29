# Credit Card Fraud Detection

Banks lose crores every year because fraud is detected too late.
I built a model that flags suspicious transactions before they go through.

Trained on 2.8 lakh real transactions — model catches 85 out of 100 fraud cases.
AUC score of 0.99 — one of the best possible scores.

The hard part was that only 0.17% transactions were fraud — so I used SMOTE
to balance the data before training.

Tried 3 models — Logistic Regression, Random Forest, XGBoost.
Random Forest won.


| Model                       | Precision |   Recall | F1-Score |
| --------------------------- | --------: | -------: | -------: |
| Logistic Regression         |      0.86 |     0.60 |     0.71 |
| Logistic Regression + SMOTE |      0.06 |     0.93 |     0.11 |
| Random Forest + SMOTE       |  **0.89** | **0.85** | **0.87** |
| XGBoost + SMOTE             |      0.74 |     0.85 |     0.79 |


## Try it yourself
👉 [Live App] :-- https://card-fraud-detector-stream-lit.streamlit.app

## Tech used
Python, Scikit-learn, SMOTE, Streamlit
