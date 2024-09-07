# ------------------------------------------
# Task: Variables
# ------------------------------------------

# 1. Creating a variable named 'pi' and storing the value 22/7 in it.

print("------------------------------------------")
pi = 22 / 7

# Checking the data type of the variable 'pi'
print(f"Value of pi: {pi}")
print(f"Data type of pi: {type(pi)}")  # This will display the data type (float)
print("------------------------------------------")

#------------------------------------------

# 2. Trying to create a variable named 'for' (this will raise an error)
# Uncommenting the below line will result in a syntax error.
# for = 4

# Explanation:
# Reserved keywords cannot be used as variable names.
print("Task 2 complete: Cannot use 'for' as a variable name, it is a reserved keyword.")
print("------------------------------------------")

#------------------------------------------

# 3. Calculating Simple Interest for 3 years.
# Define principal amount, rate of interest, and time
principal = 10000  # Example value for principal amount in your currency
rate_of_interest = 5  # Example rate of interest (5%)
time = 3  # Time in years

# Calculate simple interest using the formula: Simple Interest = (P * R * T) / 100
simple_interest = (principal * rate_of_interest * time) / 100

# Print the result
print(f"Principal: {principal}")
print(f"Rate of Interest: {rate_of_interest}%")
print(f"Time: {time} years")
print(f"Simple Interest: {simple_interest}")
print("------------------------------------------")

#------------------------------------------
