# 💳 Credit Card Fraud Detection

Banks lose millions every year because fraud is detected too late. This project uses Machine Learning to identify fraudulent credit card transactions before they are processed.

The model was trained on **284,807 real-world transactions**, where only **0.17%** were fraudulent. To handle this highly imbalanced dataset, **SMOTE** was used before training.

## 🚀 Results

- ✅ ROC-AUC Score: **0.99**
- ✅ Best Model: **Random Forest + SMOTE**

| Model | Precision | Recall | F1-Score |
|-------|----------:|-------:|---------:|
| Logistic Regression | 0.86 | 0.60 | 0.71 |
| Logistic Regression + SMOTE | 0.06 | 0.93 | 0.11 |
| **Random Forest + SMOTE** | **0.89** | **0.85** | **0.87** |
| XGBoost + SMOTE | 0.74 | 0.85 | 0.79 |

## 🛠 Tech Stack

Python • Pandas • NumPy • Scikit-learn • SMOTE • Streamlit

## 🌐 Live Demo

👉 https://card-fraud-detector-stream-lit.streamlit.app
