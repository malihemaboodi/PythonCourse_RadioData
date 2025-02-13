# Print a welcome message
print("Welcome to the Personal Budget Management Program!")

# Ask the user to enter their monthly income
monthly_income = float(input("Please enter your monthly income: "))

# Prompt the user to enter their expenses (e.g., food, rent, transportation, entertainment)
food_expense = float(input("Enter your food expenses: "))
rent_expense = float(input("Enter your rent expenses: "))
transportation_expense = float(input("Enter your transportation expenses: "))
entertainment_expense = float(input("Enter your entertainment expenses: "))

# Ask for the percentage of income the user wants to save
savings_percentage = float(input("Enter the percentage of your income you want to save: "))

# Calculate the total expenses
total_expenses = food_expense + rent_expense + transportation_expense + entertainment_expense

# Calculate the remaining budget after expenses
remaining_budget = monthly_income - total_expenses

# Calculate the amount to be saved
savings_amount = (savings_percentage / 100) * monthly_income

# Calculate the final remaining budget after saving
final_remaining_budget = remaining_budget - savings_amount

# Display the results
print("\n----- Budget Summary -----")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget (after expenses): ${remaining_budget:.2f}")
print(f"Planned Monthly Savings: ${savings_amount:.2f}")
print(f"Final Remaining Budget (after savings): ${final_remaining_budget:.2f}")