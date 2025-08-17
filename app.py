import streamlit as st
from predictor import make_prediction

st.set_page_config(page_title="LoanEP", page_icon="💰", layout="wide")

st.title(":blue[_My Loan Eligibility Predictor_]")
st.markdown(":violet[Provide your details to check if you're eligible for a loan]")

full_name = st.text_input("Full name", placeholder='enter full name')
gender = st.selectbox("Gender", ["Female", "Male"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income(₦)", min_value=0)
coapplicant_income = st.number_input("Co-applicant Income(₦)", min_value=0)
loan_amount = st.number_input("Loan Amount(in thousand ₦)", min_value=0)
loan_term = st.number_input("Loan Term (in days: 0-365)", min_value=0)
credit_history = st.selectbox("Credit History", [1, 0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

user_input = {
    "Gender": gender,
    "Married": married,
    "Dependents": dependents,
    "Education": education,
    "Self_Employed": self_employed,
    "ApplicantIncome": applicant_income,
    "CoapplicantIncome": coapplicant_income,
    "LoanAmount": loan_amount,
    "Loan_Amount_Term": loan_term,
    "Credit_History": credit_history,
    "Property_Area": property_area
}
if st.button("Check Eligibility"):
    with st.spinner("Analyzing..."):
        pred, prob = make_prediction(user_input)
        if pred == 1:
            st.success(f"Dear {full_name}, you're eligible for this loan")
        else:
            st.error(f"Dear {full_name}, sorry you're not eligible for this loan")
        st.info(f"Confidence: **{prob*100:.2f}** %")

st.markdown("---")
st.markdown("Copyright 2025")