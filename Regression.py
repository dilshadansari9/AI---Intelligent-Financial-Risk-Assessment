import streamlit as st
import pandas as pd
import numpy as np
import pickle
def Loan_Regression():
    def load_objects():
        objs = {
            'reg_lr': pickle.load(open('Reg_LR.pkl', 'rb')),
            'reg_rf': pickle.load(open('Reg_RF.pkl', 'rb')),
            'reg_xgb': pickle.load(open('Reg_XGB.pkl', 'rb')),
            'reg_ct': pickle.load(open('Reg_ct.pkl', 'rb'))
        }
        return objs
    objs=load_objects() 

    # Regression models
    reg_lr = objs['reg_lr']
    reg_rf = objs['reg_rf']
    reg_xgb = objs['reg_xgb']
    reg_ct = objs['reg_ct']


    st.title("🏦 EMI Eligibility Input Form")

    # Row 1
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, step=1, value=30)
    with col2:
        gender = st.selectbox("Gender", ["Male", "Female"])
    with col3:
        marital_status = st.selectbox("Marital Status", ["Single", "Married"])

    # Row 2
    col4, col5, col6 = st.columns(3)
    with col4:
        education = st.selectbox("Education", ['Unknown', 'High School', 'Graduate', 'Post Graduate', 'Professional'])
    with col5:
        monthly_salary = st.number_input("Monthly Salary (₹)", min_value=0, max_value=1000000, step=1000, value=50000)
    with col6:
        employment_type = st.selectbox("Employment Type", ["Private", "Government", "Self-Employed"])

    # Row 3
    col7, col8, col9 = st.columns(3)
    with col7:
        years_of_employment = st.number_input("Years of Employment", min_value=0, max_value=50, step=1, value=5)
    with col8:
        company_type = st.selectbox("Company Type", ['Mid-size', 'MNC', 'Startup', 'Large Indian', 'Small'])
    with col9:
        house_type = st.selectbox("House Type", ['Own', 'Rented', 'Family'])

    # Row 4
    col10, col11, col12 = st.columns(3)
    with col10:
        monthly_rent = st.number_input("Monthly Rent (₹)", min_value=0, max_value=100000, step=500, value=2000)
    with col11:
        family_size = st.number_input("Family Size", min_value=1, max_value=20, step=1, value=4)
    with col12:
        dependents = st.number_input("Dependents", min_value=0, max_value=10, step=1, value=1)

    # Row 5
    col13, col14, col15 = st.columns(3)
    with col13:
        school_fees = st.number_input("School Fees (₹)", min_value=0, max_value=100000, step=500, value=2000)
    with col14:
        college_fees = st.number_input("College Fees (₹)", min_value=0, max_value=100000, step=500, value=3000)
    with col15:
        travel_expenses = st.number_input("Travel Expenses (₹)", min_value=0, max_value=100000, step=500, value=1500)

    # Row 6
    col16, col17, col18 = st.columns(3)
    with col16:
        groceries_utilities = st.number_input("Groceries & Utilities (₹)", min_value=0, max_value=100000, step=500, value=4000)
    with col17:
        other_monthly_expenses = st.number_input("Other Monthly Expenses (₹)", min_value=0, max_value=100000, step=500, value=2000)
    with col18:
        existing_loans = st.selectbox("Existing Loans", ['Yes', 'No'])

    # Row 7
    col19, col20, col21 = st.columns(3)
    with col19:
        credit_score = st.number_input("Credit Score", min_value=300, max_value=850, step=10, value=700)
    with col20:
        bank_balance = st.number_input("Bank Balance (₹)", min_value=0, max_value=1000000, step=1000, value=10000)
    with col21:
        emergency_fund = st.number_input("Emergency Fund (₹)", min_value=0, max_value=1000000, step=1000, value=5000)

    # Row 8
    col22, col23, col24 = st.columns(3)
    with col22:
        emi_scenario = st.selectbox("EMI Scenario", [
            'Personal Loan EMI', 'E-commerce Shopping EMI', 'Education EMI', 'Vehicle EMI', 'Home Appliances EMI'
        ])
    with col23:
        requested_amount = st.number_input("Requested Amount (₹)", min_value=0, max_value=1000000, step=1000, value=20000)
    with col24:
        requested_tenure = st.number_input("Requested Tenure (months)", min_value=1, max_value=85, step=1, value=24)

    # Row 9
    col25, col26, col27 = st.columns(3)
    with col25:
        max_monthly_emi = st.number_input("Max Monthly EMI you can pay (₹)", min_value=2000, max_value=100000, step=1000, value=10000)
    with col26:
        employment_group = st.selectbox("Employment Group", ['0–2 yrs', '3–5 yrs', '6–10 yrs', '11–20 yrs', '20+ yrs'])
    with col27:
        affordability_ratio = st.number_input("Affordability Ratio", min_value=0.0, max_value=1.0, step=0.01, value=0.5)

    # Row 10
    col28, col29, col30 = st.columns(3)
    with col28:
        credit_risk = st.selectbox("Credit Risk", ['Low Risk', 'Medium Risk', 'High Risk'])
    with col29:
        employment_stability = st.selectbox("Employment Stability", ['Unstable', 'Moderate', 'Stable', 'Highly Stable'])
    with col30:
        st.write("")  


    input_data = {
        'age': age, 
        'gender': gender, 
        'marital_status': marital_status, 
        'education': education,
        'monthly_salary': monthly_salary, 
        'employment_type': employment_type,
        'years_of_employment': years_of_employment, 
        'company_type': company_type, 
        'house_type': house_type,
        'monthly_rent': monthly_rent, 
        'family_size': family_size, 
        'dependents': dependents,
        'school_fees': school_fees, 
        'college_fees': college_fees, 
        'travel_expenses': travel_expenses,
        'groceries_utilities': groceries_utilities, 
        'other_monthly_expenses': other_monthly_expenses,
        'existing_loans': existing_loans, 
        'credit_score': credit_score, 
        'bank_balance': bank_balance,
        'emergency_fund': emergency_fund, 
        'emi_scenario': emi_scenario, 
        'requested_amount': requested_amount,
        'requested_tenure': requested_tenure, 
        'max_monthly_emi': max_monthly_emi,
        'employment_group': employment_group, 
        'affordability_ratio': affordability_ratio,
        'credit_risk': credit_risk, 
        'employment_stability': employment_stability
    }

    input_df = pd.DataFrame([input_data])
    st.write("### Your Input Data Preview:")
    st.dataframe(input_df)


    model_choice = st.selectbox(
        "Select a Model",
        ["Linear Regression", "Random Forest Regressior", "XGBoost Regressior"]
    )

    # Prediction section
    if st.button("Predict Eligibility"):
        try:
            input_encoded = reg_ct.transform(input_df)
            if hasattr(input_encoded, "toarray"):
                input_encoded = input_encoded.toarray()

            if model_choice == "Logistic Regression":
                model = reg_lr
            elif model_choice == "Random Forest Classifier":
                model = reg_rf
            else:
                model = reg_xgb

            predict = model.predict(input_encoded)
            st.write(predict)
            # pred_label = le.inverse_transform(predict)

            # result = pred_label[0]
            # if result == "Eligible":
            #     st.success("✅ Congratulations! You are eligible for the loan.")
            # elif result == "Not Eligible":
            #     st.error("❌ Sorry, you are not eligible for the loan.")
            # else:
            #     st.warning("⚠️ High Risk! Please review your financial profile.")

            # st.write("Prediction (label):", result)

        except Exception as e:
            st.error(f"Prediction failed: {e}")
            st.info(
                "Common causes: transformer expects different column order/names or missing categories. "
                "Make sure the input DataFrame columns exactly match training feature order & names."
            )
