# ------------------------------------------
# Task: IF - Condtion
# ------------------------------------------

print("------------------------------------------")
# 1. Determine BMI Category based on user input

def calculate_bmi_category():
    # Input height in meters and weight in kilograms
    height = float(input("Enter height in meters: "))
    weight = float(input("Enter weight in kilograms: "))

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Determine BMI category
    if bmi >= 30:
        print("Obesity")
    elif 25 <= bmi < 30:
        print("Overweight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    else:
        print("Underweight")

# 2. Determine which country a city belongs to

def find_city_country():
    # Lists of cities by country
    Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
    UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
    India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

    # Input city name
    city = input("Enter a city name: ")

    # Determine country of the city
    if city in Australia:
        print(f"{city} is in Australia")
    elif city in UAE:
        print(f"{city} is in UAE")
    elif city in India:
        print(f"{city} is in India")
    else:
        print(f"{city} is not in the list")

# 3. Check if two cities belong to the same country

def check_cities_same_country():
    # Lists of cities by country
    Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
    UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
    India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

    # Input two city names
    city1 = input("Enter the first city: ")
    city2 = input("Enter the second city: ")

    # Determine which country each city belongs to
    country1 = None
    country2 = None

    if city1 in Australia:
        country1 = "Australia"
    elif city1 in UAE:
        country1 = "UAE"
    elif city1 in India:
        country1 = "India"

    if city2 in Australia:
        country2 = "Australia"
    elif city2 in UAE:
        country2 = "UAE"
    elif city2 in India:
        country2 = "India"

    # Check if both cities belong to the same country
    if country1 and country2:
        if country1 == country2:
            print(f"Both cities are in {country1}")
        else:
            print("They don't belong to the same country")
    else:
        print("One or both of the cities are not in the list")

# Run the functions
print("BMI Category Calculator")
calculate_bmi_category()
print("------------------------------------------")
print("\nCity Country Finder")
find_city_country()
print("------------------------------------------")
print("\nCheck Cities Same Country")
check_cities_same_country()
print("------------------------------------------")
