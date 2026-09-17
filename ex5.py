import streamlit as st

# 1. Display the fruits inside a selection dropdown box
fruits = ["Apple", "Orange", "Banana"]
selected_fruit = st.selectbox("Select a fruit:", fruits)

# 2. Display the selected fruit
st.write(f"You selected: **{selected_fruit}**")