import streamlit as st

st.title("Stationery Shop POS System")

# Initialize shopping cart in session state if it doesn't exist
if "cart" not in st.session_state:
    st.session_state.cart = []
if "checked_out" not in st.session_state:
    st.session_state.checked_out = False

# 1. Enter customer name
customer_name = st.text_input("Enter customer name:", disabled=st.session_state.checked_out)

# Price catalog setup
items_catalog = {
    "Pen (RM2)": 2,
    "Notebook (RM5)": 5,
    "Marker (RM4)": 4
}

# Only display shopping controls if checkout hasn't been completed
if not st.session_state.checked_out:
    # 2. Select a stationery item
    selected_item = st.selectbox("Select a stationery item:", list(items_catalog.keys()))
    
    # 3. Enter the quantity
    quantity = st.number_input("Enter quantity:", min_value=1, value=1, step=1)
    
    # 4. Click Add Item to continue shopping
    if st.button("Add Item"):
        unit_price = items_catalog[selected_item]
        subtotal = unit_price * quantity
        # Save structural details to cart list
        st.session_state.cart.append({
            "item": selected_item,
            "qty": quantity,
            "subtotal": subtotal
        })
        st.success(f"Added {quantity}x {selected_item} to cart!")

# Render current active cart items
if st.session_state.cart:
    st.write("### Current Shopping Cart")
    total_payment = 0
    for idx, cart_item in enumerate(st.session_state.cart):
        st.write(f"{idx+1}. {cart_item['item']} x {cart_item['qty']} = RM {cart_item['subtotal']:.2f}")
        total_payment += cart_item['subtotal']
        
    st.write(f"**Current Total: RM {total_payment:.2f}**")

    # 5. Repeat until user clicks Checkout button
    if not st.session_state.checked_out:
        if st.button("Checkout"):
            st.session_state.checked_out = True
            st.rerun()

# 6. Final display layout state post-checkout
if st.session_state.checked_out:
    st.success("### Final Receipt")
    st.write(f"Customer Name: **{customer_name}**")
    final_total = sum(item['subtotal'] for item in st.session_state.cart)
    st.write(f"## Total Final Payment: RM {final_total:.2f}")
    
    # Optional Reset button to clear shop layout
    if st.button("New Transaction"):
        st.session_state.cart = []
        st.session_state.checked_out = False
        st.rerun()