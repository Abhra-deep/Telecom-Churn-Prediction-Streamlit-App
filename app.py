import streamlit as st
import pandas as pd
import pickle
import os

# 🚀 Debug start
st.write("🚀 App started")

# Load model safely
try:
    model_path = os.path.join(os.path.dirname(__file__), 'randomforest.pkl')
    model = pickle.load(open(model_path, 'rb'))
    st.write("✅ Model loaded successfully")
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()   # ⛔ Stop app if model fails

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

    # Inputs
    tenure = st.slider("Tenure (months)", 0, 100, 1)

    phone_service = st.selectbox("Phone Service", [0, 1])
    st.caption("0: No, 1: Yes")

    contract = st.selectbox("Contract", [0, 1, 2])
    st.caption("0: Month-to-month, 1: One year, 2: Two year")

    paperless_billing = st.selectbox("Paperless Billing", [0, 1])
    st.caption("0: No, 1: Yes")

    payment_method = st.selectbox("Payment Method", [0, 1, 2, 3])
    st.caption("0: Bank transfer, 1: Credit card, 2: Electronic check, 3: Mailed check")

    monthly_charges = st.number_input("Monthly Charges", min_value=0.0)

    input_data = {
        'tenure': tenure,
        'PhoneService': phone_service,
        'Contract': contract,
        'PaperlessBilling': paperless_billing,
        'PaymentMethod': payment_method,
        'MonthlyCharges': monthly_charges
    }

    # Prediction button
    if st.button("Predict"):
        try:
            prediction, probability = predict_churn(input_data)

            st.subheader("🔍 Result")

            if probability >= 0.4:
                st.error("Customer is likely to churn ⚠️")
            else:
                st.success("Customer is unlikely to churn ✅")

            st.write(f"📊 Churn Probability: {probability:.2f}")

        except Exception as e:
            st.error(f"❌ Prediction error: {e}")

# Run app
if __name__ == '__main__':
    main()
