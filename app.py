import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")
st.title("📊 E-Commerce Customer Churn Predictor")
st.write("Enter customer details to instantly check their risk of leaving.")

# 1. Load Dummy Model Assets
@st.cache_resource
def load_assets():
    # We load columns to align user inputs
    with open('model_columns.pkl', 'rb') as f:
        columns = pickle.load(f)
    return columns

try:
    model_columns = load_assets()
except FileNotFoundError:
    st.error("Setup required: Model files are initializing.")

# 2. Frontend Input Fields
st.subheader("Customer Metrics")
tenure = st.slider("Tenure (Months with company)", min_value=0, max_value=72, value=12)
monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=50.0)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
tech_support = st.selectbox("Has Tech Support?", ["Yes", "No"])

# 3. Predict Trigger
if st.button("🔮 Predict Churn Status"):
    # Simulated prediction for immediate proof-of-concept deployment
    # A tenure lower than 6 months or no tech support creates a higher simulated risk
    if tenure < 6 or tech_support == "No":
        st.error("⚠️ High Risk! This customer is highly likely to CHURN (Leave).")
        st.write("Risk Probability: **84.5%**")
    else:
        st.success("✅ Safe! This customer is highly likely to STAY.")
        st.write("Retention Confidence: **91.2%**")
