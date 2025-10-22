import streamlit as st
from Classification import Loan_classification
from Regression import Loan_Regression


st.title("🏦 EMI Prediction App")
st.write("Welcome to the EMI Prediction App! 👋")
st.markdown("""
    This app helps you:
    1. Predict whether you are eligible for a loan.  
    2. If eligible, estimate your **maximum EMI** using regression models.
    """)


st.sidebar.title("Navigation")
option = st.sidebar.selectbox('Select an Option', ['Home', 'Loan Classification', 'Loan EMI Prediction'])


if option=='Loan Classification':
    Loan_classification()
elif option=='Loan EMI Prediction':
    Loan_Regression() 
