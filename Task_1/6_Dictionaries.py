# ------------------------------------------
# Task: DICTIONARIES
# ------------------------------------------

# ------------------------------------------
# Task 1: List of Friends and Length of Names
# ------------------------------------------

# Create a list of friends' names
friends = ["John", "Aditya", "Maria", "Samuel", "Ayesha"]

# Create a list of tuples with (friend's name, length of the name)
friends_name_length = [(name, len(name)) for name in friends]

# Print the list of tuples
print("------------------------------------------")
print("Friends' Names and Lengths:")
for friend in friends_name_length:
    print(friend)
print("------------------------------------------")

# ------------------------------------------
# Task 2: Trip Expense Tracker
# ------------------------------------------

# Create dictionaries for your expenses and your partner's expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate the total expenses for each
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

# Print total expenses
print("Your total expenses:", your_total)
print("Your partner's total expenses:", partner_total)
print("------------------------------------------")

# Determine who spent more money overall
if your_total > partner_total:
    print("You spent more money overall.")
elif partner_total > your_total:
    print("Your partner spent more money overall.")
else:
    print("Both spent the same amount.")
print("------------------------------------------")

# Find the expense category with significant difference
print("Significant differences in expenses:")
for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])
    if difference > 100:  # Assuming a difference of more than 100 is significant
        print(f"{category}: Difference of {difference}")
print("------------------------------------------")
