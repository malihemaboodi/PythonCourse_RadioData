import streamlit as st


st.title("Personal Budget Management Program")
st.write("Welcome to the Personal Budget Management Program! Let's manage your budget.")


monthly_income = st.number_input("Please enter your monthly income:", min_value=0.0, format="%.2f")

food_expense = st.number_input("Enter your food expenses:", min_value=0.0, format="%.2f")
rent_expense = st.number_input("Enter your rent expenses:", min_value=0.0, format="%.2f")
transport_expense = st.number_input("Enter your transportation expenses:", min_value=0.0, format="%.2f")
entertainment_expense = st.number_input("Enter your entertainment expenses:", min_value=0.0, format="%.2f")

savings_percentage = st.number_input("Enter the percentage of income you want to save:", min_value=0.0, max_value=100.0, format="%.2f")


total_expenses = food_expense + rent_expense + transport_expense + entertainment_expense


savings_amount = (savings_percentage / 100) * monthly_income


remaining_budget = monthly_income - total_expenses


st.subheader("Results:")


st.write(f"Total Expenses: ${total_expenses:.2f}")
st.write(f"Remaining Budget: ${remaining_budget:.2f}")
st.write(f"Monthly Savings: ${savings_amount:.2f}")


if remaining_budget >= savings_amount:
    st.write("Budget Status: You are under budget!")
else:
    st.write(f"Budget Status: You have exceeded your budget by ${abs(remaining_budget):.2f}.")
