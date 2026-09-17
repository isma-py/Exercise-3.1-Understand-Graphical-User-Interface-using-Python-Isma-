import streamlit as st

st.title("Gym Membership Registration")

# 1. Enter member name
member_name = st.text_input("Enter member name:")

# 2. Select membership plan
plans = {
    "Monthly (RM80)": 80,
    "Quarterly (RM220)": 220,
    "Yearly (RM800)": 800
}
selected_plan = st.selectbox("Select membership plan:", list(plans.keys()))

# 3. Display membership fee details
fee = plans[selected_plan]

if member_name:
    st.subheader("Registration Confirmed")
    st.write(f"Member Name: **{member_name}**")
    st.write(f"Selected Plan: **{selected_plan}**")
    st.write(f"### Membership Fee to Pay: RM {fee}")