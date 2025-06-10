import streamlit as st
import math

st.set_page_config(page_title="OmegaCalc", page_icon="🧠")

st.title("🧠 OmegaCalc")
st.subheader("Your Friendly AI-Powered Calculator")

# User selects operation
operation = st.selectbox("Choose an operation:", [
    "Add", "Subtract", "Multiply", "Divide", "Exponent", "Modulo", "Square Root", "Floor Division"
])

# History tracking
if 'history' not in st.session_state:
    st.session_state.history = []

# Input fields
if operation == "Square Root":
    num1 = st.number_input("Enter a number:", step=1.0)
else:
    num1 = st.number_input("Enter the first number:", step=1.0)
    num2 = st.number_input("Enter the second number:", step=1.0)

# Perform calculation
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        symbol = "+"
    elif operation == "Subtract":
        result = num1 - num2
        symbol = "-"
    elif operation == "Multiply":
        result = num1 * num2
        symbol = "*"
    elif operation == "Divide":
        result = "Error" if num2 == 0 else num1 / num2
        symbol = "/"
    elif operation == "Exponent":
        result = num1 ** num2
        symbol = "^"
    elif operation == "Modulo":
        result = num1 % num2
        symbol = "%"
    elif operation == "Floor Division":
        result = "Error" if num2 == 0 else num1 // num2
        symbol = "//"
    elif operation == "Square Root":
        result = "Error" if num1 < 0 else math.sqrt(num1)
        symbol = "√"
    
    # Save to history
    if operation == "Square Root":
        calc = f"√{num1} = {result}"
    else:
        calc = f"{num1} {symbol} {num2} = {result}"

    st.session_state.history.append(calc)
    st.success(f"Result: {result}")

# Show history
if st.checkbox("Show history"):
    st.subheader("📝 Calculation History")
    for item in st.session_state.history:
        st.write(item)
