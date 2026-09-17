import streamlit as st

# 1. Select your gender using radio buttons
gender_options = ["Male", "Female"]
gender = st.radio("Select your gender:", gender_options)

# 2. Display the selected gender
st.write(f"Selected Gender: **{gender}**")