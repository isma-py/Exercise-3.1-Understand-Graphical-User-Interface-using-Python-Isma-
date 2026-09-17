import streamlit as st

st.title("Total Calculator")

# 1. Enter two numbers
num1 = st.number_input("Enter first number:", value=0.0)
num2 = st.number_input("Enter second number:", value=0.0)

# 2. Display the total
total = num1 + num2
st.write(f"**Total:** {total}")