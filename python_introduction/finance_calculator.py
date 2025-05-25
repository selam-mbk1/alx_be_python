# finance_calculator.py

# Prompt the user for input
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Calculate projected savings after one year with 5% interest
projected_savings = monthly_savings * 12 * 1.05

# Display the results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
