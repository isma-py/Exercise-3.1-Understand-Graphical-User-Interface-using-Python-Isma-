import streamlit as st

st.title("Hotel Room Booking System")

# 1. Enter customer name
customer_name = st.text_input("Enter customer name:")

# 2. Select room type with corresponding prices
room_prices = {
    "Standard (RM120)": 120,
    "Deluxe (RM180)": 180,
    "Suite (RM250)": 250
}
selected_room = st.selectbox("Select room type:", list(room_prices.keys()))

# 3. Enter number of nights
nights = st.number_input("Enter number of nights:", min_value=1, value=1, step=1)

# Calculate total
price_per_night = room_prices[selected_room]
total_payment = price_per_night * nights

# 4. Display summary and total payment
if customer_name:
    st.subheader("Booking Receipt Summary")
    st.write(f"Customer Name: **{customer_name}**")
    st.write(f"Room Type: **{selected_room}**")
    st.write(f"Nights Stayed: **{nights}**")
    st.write(f"### Total Payment: RM {total_payment}")