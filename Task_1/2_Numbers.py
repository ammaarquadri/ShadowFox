# ------------------------------------------
# Task: Numbers
# ------------------------------------------

# 1. Write a function that takes two arguments, 145 and 'o',
# and uses the `format` function to return a formatted string.

print("------------------------------------------")
def format_number(number, base):
    if base == 'o':  # If 'o' is provided, use octal representation
        formatted = format(number, 'o')  # Octal representation
    else:
        formatted = format(number, base)  # Use base provided
    return formatted

# Calling the function
number = 145
base = 'o'
formatted_output = format_number(number, base)
print(f"Formatted output: {formatted_output}")  # Should return octal representation
print("------------------------------------------")

#------------------------------------------

# 2. In a village, there is a circular pond with a radius of 84 meters.
# Calculate the area of the pond using the formula: Circle Area = π r^2.
# (Use the value 3.14 for π)
radius = 84
pi = 3.14
pond_area = pi * (radius ** 2)
print(f"Pond Area: {pond_area}")

# Bonus Question: If there is exactly 1.4 liters of water in a square meter,
# what is the total amount of water in the pond?
water_per_sqm = 1.4
total_water = pond_area * water_per_sqm
print(f"Total amount of water in the pond (without decimals): {int(total_water)}")
print("------------------------------------------")

#------------------------------------------

# 3. If you cross a 490 meter long street in 7 minutes,
# calculate your speed in meters per second.
distance = 490  # in meters
time_minutes = 7
time_seconds = time_minutes * 60  # Convert time to seconds
speed = distance / time_seconds
print(f"Speed (without decimals): {int(speed)} m/s")
print("------------------------------------------")
