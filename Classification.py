import streamlit as st
import pandas as pd
import numpy as np
import pickle

def Loan_classification():
    # Load all objects
    def load_objects():
        objs = {
            'log_reg': pickle.load(open('CL_Log_reg_model.pkl', 'rb')),
            'rf': pickle.load(open('CL_RF_model.pkl', 'rb')),
            'xgb': pickle.load(open('CL_XGB_model.pkl', 'rb')),
            'ct': pickle.load(open('CL_ct.pkl', 'rb')),
            'le': pickle.load(open('CL_le.pkl', 'rb')),
        }
        return objs


    objs = load_objects()

    # Classification models
    log_reg = objs['log_reg']
    rf_clf = objs['rf']
    xgb_clf = objs['xgb']
    ct = objs['ct']
    le = objs['le']


    # Streamlit App
    st.title("🏦 Loan Eligibility Prediction App")
    st.write("Fill the details to know whether you are eligible or not for the loan!")
    st.write("Please enter the following details:")

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
        max_monthly_emi = st.number_input("Max Monthly EMI you can pay (₹)", min_value=2000, max_value=100000, step=1000, value=10000)

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
        current_emi_amount = st.number_input("Current EMI Amount (₹)", min_value=0, max_value=100000, step=1000, value=5000)
    with col20:
        credit_score = st.number_input("Credit Score", min_value=300, max_value=850, step=10, value=700)
    with col21:
        bank_balance = st.number_input("Bank Balance (₹)", min_value=0, max_value=1000000, step=1000, value=10000)

    # Row 8
    col22, col23, col24 = st.columns(3)
    with col22:
        emergency_fund = st.number_input("Emergency Fund (₹)", min_value=0, max_value=1000000, step=1000, value=5000)
    with col23:
        emi_scenario = st.selectbox("EMI Scenario", [
            'Personal Loan EMI', 'E-commerce Shopping EMI', 'Education EMI', 'Vehicle EMI', 'Home Appliances EMI'
        ])
    with col24:
        requested_amount = st.number_input("Requested Amount (₹)", min_value=0, max_value=1000000, step=1000, value=20000)

    # Row 9
    col25, col26, col27 = st.columns(3)
    with col25:
        requested_tenure = st.number_input("Requested Tenure (months)", min_value=1, max_value=85, step=1, value=24)
    with col26:
        employment_group = st.selectbox("Employment Group", ['0–2 yrs', '3–5 yrs', '6–10 yrs', '11–20 yrs', '20+ yrs'])
    with col27:
        credit_risk = st.selectbox("Credit Risk", ['Medium Risk', 'Low Risk', 'High Risk'])

    # Row 10
    col28, col29, _ = st.columns(3)
    with col28:
        employment_stability = st.selectbox("Employment Stability", ['Unstable', 'Stable', 'Moderate', 'Highly Stable'])

    # Derived features
    dependents = family_size - 1
    total_expenses = (
        school_fees + college_fees + travel_expenses + groceries_utilities +
        other_monthly_expenses + current_emi_amount + monthly_rent
    )
    expense_to_income_ratio = total_expenses / monthly_salary if monthly_salary > 0 else 0
    affordability_ratio = max_monthly_emi / requested_amount if requested_amount > 0 else 0

    # Input dictionary
    input_dict = {
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
        'current_emi_amount': current_emi_amount,
        'credit_score': credit_score,
        'bank_balance': bank_balance,
        'emergency_fund': emergency_fund,
        'emi_scenario': emi_scenario,
        'requested_amount': requested_amount,
        'requested_tenure': requested_tenure,
        'max_monthly_emi': max_monthly_emi,
        'total_expenses': total_expenses,
        'expense_to_income_ratio': expense_to_income_ratio,
        'employment_group': employment_group,
        'affordability_ratio': affordability_ratio,
        'credit_risk': credit_risk,
        'employment_stability': employment_stability
    }

    input_df = pd.DataFrame([input_dict])

    st.write("### Your Input (Preview):")
    st.dataframe(input_df)

    model_choice = st.selectbox(
        "Select a Model",
        ["Logistic Regression", "Random Forest Classifier", "XGBoost Classifier"]
    )

    # Prediction section
    if st.button("Predict Eligibility"):
        try:
            input_encoded = ct.transform(input_df)
            if hasattr(input_encoded, "toarray"):
                input_encoded = input_encoded.toarray()

            if model_choice == "Logistic Regression":
                model = log_reg
            elif model_choice == "Random Forest Classifier":
                model = rf_clf
            else:
                model = xgb_clf

            predict = model.predict(input_encoded)
            pred_label = le.inverse_transform(predict)

            result = pred_label[0]
            if result == "Eligible":
                st.success("✅ Congratulations! You are eligible for the loan.")
            elif result == "Not Eligible":
                st.error("❌ Sorry, you are not eligible for the loan.")
            else:
                st.warning("⚠️ High Risk! Please review your financial profile.")

            st.write("Prediction (label):", result)

        except Exception as e:
            st.error(f"Prediction failed: {e}")
            st.info(
                "Common causes: transformer expects different column order/names or missing categories. "
                "Make sure the input DataFrame columns exactly match training feature order & names."
            )
