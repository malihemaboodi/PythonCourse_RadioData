import streamlit as st

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "❌ Cannot divide by zero"
    return n1 / n2

operations = {
    "➕ Addition": add,
    "➖ Subtraction": subtract,
    "✖ Multiplication": multiply,
    "➗ Division": divide,
}

st.set_page_config(page_title="🧮 Fancy Calculator", layout="centered")
st.title("🧮 Fancy Calculator 🎨")
st.markdown("### Perform basic arithmetic operations with a beautiful UI ✨")

first_number = st.number_input("🔢 Enter the first number:", value=0.0, format="%.2f")
operation = st.selectbox("📌 Choose an operation:", list(operations.keys()))
second_number = st.number_input("🔢 Enter the second number:", value=0.0, format="%.2f")

if st.button("🎯 Calculate"):
    result = operations[operation](first_number, second_number)
    st.success(f"✅ Result: {first_number} {operation.split()[0]} {second_number} = {result} 🎉")
