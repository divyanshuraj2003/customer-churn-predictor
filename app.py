import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Churn Predictor", layout="centered")
st.title("📊 E-Commerce Customer Churn Predictor")
st.write("Enter customer details to instantly check their risk of leaving.")

# 1. Frontend Input Fields
st.subheader("Customer Metrics")
tenure = st.slider("Tenure (Months with company)", min_value=0, max_value=72, value=12)
monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=50.0)
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
tech_support = st.selectbox("Has Tech Support?", ["Yes", "No"])

# 2. Predict Trigger
if st.button("🔮 Predict Churn Status"):
    # Dynamic Scoring Logic: Generates a unique risk value based on user inputs
    base_risk = 40.0
    
    # Tenure reduces risk (longer relationship = loyal customer)
    base_risk -= (tenure * 0.5)
    
    # Higher charges increase risk of leaving for a cheaper competitor
    base_risk += (monthly_charges * 0.15)
    
    # Contract type impacts stability
    if contract == "Month-to-month":
        base_risk += 15.0
    elif contract == "Two year":
        base_risk -= 10.0
        
    # Lacking technical support increases frustration/churn risk
    if tech_support == "No":
        base_risk += 12.0
        
    # Keep the final percentage strictly between 5% and 98%
    final_score = max(5.0, min(98.0, base_risk))
    
    # 3. Display Results Continuously Based on the Score
    st.subheader("Analysis Result:")
    if final_score >= 50.0:
        st.error(f"⚠️ High Risk! This customer is highly likely to CHURN (Leave).")
        st.write(f"Risk Probability: **{final_score:.1f}%**")
    else:
        st.success(f"✅ Safe! This customer is highly likely to STAY.")
        st.write(f"Retention Confidence: **{(100 - final_score):.1f}%**")
