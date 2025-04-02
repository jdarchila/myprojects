#You are given a monthly budget and some expenses and need to check if the sum of the expenses goes over budget! 

# First, store the total of all expenses into a variable called total.

#Next, check if the total is greater than the budget. If it is, store True into a variable called over_budget, otherwise store False in over_budget.

# Monthly budget
budget = 2000

# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

# Calculate the total amount of expenses

total = food_bill + electricity_bill + internet_bill + rent

# Check if the total is greater than the budget and store the result in over_budget

if total > budget:
    over_budget = True
else:
    over_budget = False

print("Total: " + str(total))
print("Is it over budget? " + str(over_budget))   


