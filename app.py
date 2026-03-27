import streamlit as st
import pandas as pd
import pickle
import os

# Load model safely
try:
    model_path = os.path.join(os.path.dirname(__file__), 'randomforest.pkl')
    model = pickle.load(open(model_path, 'rb'))
except Exception as e:
    st.error(f"Error loading model: {e}")

# Define columns
columns = ['tenure', 'PhoneService', 'Contract',
           'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges']

# Prediction function
def predict_churn(input_data):
    input_df = pd.DataFrame([input_data], columns=columns)
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)[:, 1]
    return prediction[0], probability[0]

# App
def main():
    st.set_page_config(page_title="Churn Predictor", layout="centered")

    st.title("📊 Telecom Churn Prediction")
    st.write("Enter customer details to predict churn.")

    tenure = st.slider("Tenure (months)", 0, 100, 1)

    phone_service = st.selectbox("Phone Service", [0, 1])
    contract = st.selectbox("Contract", [0, 1, 2])
    paperless_billing = st.selectbox("Paperless Billing", [0, 1])
    payment_method = st.selectbox("Payment Method", [0, 1, 2, 3])
    monthly_charges = st.number_input("Monthly Charges")

    input_data = {
        'tenure': tenure,
        'PhoneService': phone_service,
        'Contract': contract,
        'PaperlessBilling': paperless_billing,
        'PaymentMethod': payment_method,
        'MonthlyCharges': monthly_charges
    }

    if st.button("Predict"):
        prediction, probability = predict_churn(input_data)

        st.subheader("🔍 Result")

        if probability >= 0.4:
            st.error("Customer is likely to churn ⚠️")
        else:
            st.success("Customer is unlikely to churn ✅")

        st.write(f"Churn Probability: {probability:.2f}")

# Run
if __name__ == '__main__':
    main()
