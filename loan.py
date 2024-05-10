import streamlit as st
st.set_page_config(
    page_title="bbot_loan",
    page_icon="💸",
)
def update_credit_score_value():
    st.markdown('<style>div[data-baseweb="slider"] > div > div > div { background-color: #adb151 !important; }</style>', unsafe_allow_html=True)
    credit_score_value = st.slider("Credit Score", min_value=100, max_value=700, step=1, key='credit_score')
    return credit_score_value

def update_interest_rate_value():
    interest_rate_value = st.number_input("Expected Interest Rate (%)", min_value=0.0, max_value=20.0, step=None)
    return interest_rate_value

def eligibility(age, annual_income, loan_amount, employment_status, credit_score, expected_interest, loan_purpose):
    maximum_age = 58
    tenure = maximum_age - age
    income_portion = (40 / 100) * annual_income
    eligible_amount = tenure * income_portion

    # Eligibility logic based on loan purpose
    if loan_purpose == "Personal Loan":
        if credit_score > 375 and annual_income > 120000:
            if 2 <= tenure <= 40:
                if eligible_amount > loan_amount:
                    return True, f"Congratulations! You are eligible for the loan. The eligible loan amount for you is Rs. {eligible_amount}"
                else:
                    return False, "You are not eligible for the loan. Your eligible amount is less than your required loan amount."
            else:
                return False, f"Your tenure age doesn't fit the ideal one. Still, the eligible loan amount for you is Rs. {eligible_amount}"
        else:
            return False, "You are not eligible for the loan. Either your annual income is less than the eligible annual income or your credit score is less."

    elif loan_purpose == "Debt Consolidation Loan":
        if credit_score > 375 and annual_income > 120000:
            if 2 <= tenure <= 40:
                return True, f"Congratulations! You are eligible for the loan. The eligible loan amount for you is Rs. {eligible_amount}"
            else:
                return False, f"Your tenure age doesn't fit the ideal one. Still, the eligible loan amount for you is Rs. {eligible_amount}"
        else:
            return False, "You are not eligible for the loan. Either your annual income is less than the eligible annual income or your credit score is less."

    # Add more loan types with their specific eligibility criteria here

if __name__ == "__main__":
    st.title("Loan Eligibility Checker")

    # Main content
    col1, col2, col3 = st.columns([2, 4, 2])
    with col1:
        st.image("loan.png", use_column_width=True, width=300)
    with col2:
        age = st.number_input("Age", min_value=18, max_value=100, step=1)
        annual_income = st.number_input("Annual Income", min_value=0, step=1000)
        loan_amount = st.number_input("Loan Amount", min_value=0, step=1000)
        employment_status = st.selectbox("Employment Status", ["Employed", "Self-Employed"])
        credit_score = update_credit_score_value()
        loan_purpose = st.selectbox("Loan Purpose", ["Personal Loan", "Debt Consolidation Loan", "Mortgage", "Home Loan", "Student Loan", "Auto Loan", "Small Business Loan", "Credit Builder Loan", "Payday Loan"])

        expected_interest = update_interest_rate_value()

    with col3:
        col_submit = st.columns(1)
        with col_submit[0]:
            st.write("")  # Empty space to align with the first line
            if st.button("Submit"):
                is_eligible, message = eligibility(age, annual_income, loan_amount, employment_status, credit_score, expected_interest, loan_purpose)
                if is_eligible:
                    st.success(message)
                else:
                    st.error(message)
            if st.button("Clear"):
                st.caching.clear_cache()
