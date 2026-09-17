import streamlit as st

# 1. Enter your name
name = st.text_input("Enter your name:")

# 2. Display the entered name
if name:
    st.write(f"Hello, {name}!")