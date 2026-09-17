import streamlit as st

st.title("Combined Streamlit Exercises (1-6)")

# Create tabs for each exercise
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Exercise 1", 
    "Exercise 2", 
    "Exercise 3", 
    "Exercise 4", 
    "Exercise 5", 
    "Exercise 6"
])

# ==========================================
# Exercise 1: Display a Title
# ==========================================
with tab1:
    st.header("Exercise 1: Display a Title")
    st.title("Python GUI Application")

# ==========================================
# Exercise 2: Display Text
# ==========================================
with tab2:
    st.header("Exercise 2: Display Text")
    st.text("Student Name: John Doe")
    st.text("Programme: Bachelor of Computer Science")

# ==========================================
# Exercise 3: Text Input
# ==========================================
with tab3:
    st.header("Exercise 3: Text Input")
    
    # 1. Enter your name
    name = st.text_input("Enter your name:", key="ex3_name")
    
    # 2. Display the entered name
    if name:
        st.write(f"Hello, {name}!")

# ==========================================
# Exercise 4: Number Input
# ==========================================
with tab4:
    st.header("Exercise 4: Number Input")
    
    # 1. Enter two numbers
    num1 = st.number_input("Enter first number:", value=0.0, key="ex4_num1")
    num2 = st.number_input("Enter second number:", value=0.0, key="ex4_num2")
    
    # 2. Display the total
    total = num1 + num2
    st.write(f"**Total:** {total}")

# ==========================================
# Exercise 5: User Event (Dropdown)
# ==========================================
with tab5:
    st.header("Exercise 5: User Event")
    
    # 1. Display the fruits
    fruits = ["Apple", "Orange", "Banana"]
    selected_fruit = st.selectbox("Select a fruit:", fruits, key="ex5_fruit")
    
    # 2. Display the selected fruit
    st.write(f"You selected: **{selected_fruit}**")

# ==========================================
# Exercise 6: User Event (Radio Buttons)
# ==========================================
with tab6:
    st.header("Exercise 6: User Event")
    
    # 1. Select your gender
    gender_options = ["Male", "Female"]
    gender = st.radio("Select your gender:", gender_options, key="ex6_gender")
    
    # 2. Display the selected gender
    st.write(f"Selected Gender: **{gender}**")