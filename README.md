# Telecom Churn Prediction System

A machine learning web application that predicts whether a telecom customer is likely to churn, built using Python, Scikit-learn, and Streamlit.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Click%20Here-brightgreen)](https://telecom-churn-prediction-app-abhradeep.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-abhra--deep-blue)](https://github.com/abhra-deep/Telecom-Churn-Prediction-Streamlit-App)
![](https://img.shields.io/badge/Maintained-Yes-indigo)

---

## 📌 About The Project

Customer churn is one of the biggest challenges for telecom companies. This project builds an end-to-end machine learning pipeline that:

- Analyzes customer data (contract type, tenure, billing, services)
- Predicts churn probability using a trained Random Forest model
- Displays results in a clean, interactive web interface

Built as part of my AI/ML portfolio to demonstrate real-world machine learning deployment skills.

---

## 🚀 Live Demo

👉 [Click here to try the app](https://telecom-churn-prediction-app-abhradeep.streamlit.app/)

Enter customer details and instantly see:
- Whether the customer is likely to churn
- The probability score of churn

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| ML Model | Random Forest (Scikit-learn) |
| Frontend | Streamlit |
| Deployment | Streamlit Cloud |
| Data | IBM Telco Customer Churn Dataset (Kaggle) |

---

## 📊 Dataset

- **Source:** [Kaggle - Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- **Rows:** 7,043 customers
- **Features:** 21 columns including tenure, contract type, payment method, monthly charges
- **Target:** Churn (Yes/No)

---

## 🧠 Model Details

- **Algorithm:** Random Forest Classifier
- **Input Features:**
  - Tenure (months)
  - Phone Service
  - Contract Type (Month-to-month / One year / Two year)
  - Paperless Billing
  - Payment Method
  - Monthly Charges
- **Output:** Churn prediction + probability score
- **Threshold:** 0.4 (optimized for recall to catch at-risk customers)

---

## ⚙️ Run Locally

```bash
# Clone the repository
git clone https://github.com/abhra-deep/Telecom-Churn-Prediction-Streamlit-App.git

# Go into the folder
cd Telecom-Churn-Prediction-Streamlit-App

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
Telecom-Churn-Prediction-Streamlit-App/
│
├── app.py               # Streamlit web app
├── randomforest.pkl     # Trained ML model
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 📬 Contact

**Abhradeep Chandra Paul**
- 📧 abhradeepchandrapaul@gmail.com
- 💼 [LinkedIn](https://linkedin.com/in/abhradeepchandrapaul)
- 🐙 [GitHub](https://github.com/abhra-deep)

---

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">If you found this useful, please ⭐ the repo!</div>
