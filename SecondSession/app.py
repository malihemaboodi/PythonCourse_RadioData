import streamlit as st

# Title and introduction
st.title("💰 Personal Budget Management Program")
st.write("Welcome to the **Personal Budget Management Program**! Let's manage your budget and plan your savings effectively. 🏦")

# Input Fields with Styling
st.markdown("### 📊 **Enter your financial details:**")

monthly_income = st.number_input("💵 **Monthly Income**", min_value=0.0, format="%.2f", help="Enter your total monthly income.")
food_expense = st.number_input("🍔 **Food Expenses**", min_value=0.0, format="%.2f", help="Enter your monthly food expenses.")
rent_expense = st.number_input("🏠 **Rent Expenses**", min_value=0.0, format="%.2f", help="Enter your monthly rent expenses.")
transport_expense = st.number_input("🚗 **Transportation Expenses**", min_value=0.0, format="%.2f", help="Enter your monthly transportation expenses.")
entertainment_expense = st.number_input("🎉 **Entertainment Expenses**", min_value=0.0, format="%.2f", help="Enter your monthly entertainment expenses.")

savings_percentage = st.number_input("💸 **Savings Percentage**", min_value=0.0, max_value=100.0, format="%.2f", help="Enter the percentage of your income you'd like to save.")

# Calculations
total_expenses = food_expense + rent_expense + transport_expense + entertainment_expense
savings_amount = (savings_percentage / 100) * monthly_income
remaining_budget = monthly_income - total_expenses

# Results Section with Styling
st.markdown("### 📈 **Budget Summary:**")

st.write(f"**Total Expenses:** 💵 ${total_expenses:.2f}")
st.write(f"**Remaining Budget:** 💚 ${remaining_budget:.2f}")
st.write(f"**Monthly Savings:** 🏦 ${savings_amount:.2f}")

# Progress Bar to show Budget Status
progress = remaining_budget / monthly_income if remaining_budget >= 0 else 0
st.progress(progress)

# Budget Status Message
if remaining_budget >= savings_amount:
    st.success("🎉 **You are under budget and on track with your savings!**")
else:
    st.error(f"❌ **You have exceeded your budget by ${abs(remaining_budget):.2f}. Please adjust your expenses.**")

