# ------------------------------------------
# Task: Representing Avengers Team Using Classes
# ------------------------------------------

# Creating the Avenger class
class Avenger:
    def __init__(self, name, age, gender, super_power, weapon, leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.leader = leader
    
    # Method to get information about the superhero
    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Super Power: {self.super_power}")
        print(f"Weapon: {self.weapon}")
        print("------------------------------------------")
    
    # Method to check if the superhero is the leader
    def is_leader(self):
        if self.leader:
            print(f"{self.name} is the leader of the Avengers.")
        else:
            print(f"{self.name} is not the leader of the Avengers.")
        print("------------------------------------------")

# Creating the list of superheroes
super_heroes = [
    {"name": "Captain America", "age": 100, "gender": "Male", "super_power": "Super Strength", "weapon": "Shield", "leader": True},
    {"name": "Iron Man", "age": 50, "gender": "Male", "super_power": "Technology", "weapon": "Armor"},
    {"name": "Black Widow", "age": 35, "gender": "Female", "super_power": "Superhuman", "weapon": "Batons"},
    {"name": "Hulk", "age": 45, "gender": "Male", "super_power": "Unlimited Strength", "weapon": "No Weapon"},
    {"name": "Thor", "age": 1500, "gender": "Male", "super_power": "Super Energy", "weapon": "Mjölnir"},
    {"name": "Hawkeye", "age": 40, "gender": "Male", "super_power": "Fighting Skills", "weapon": "Bow and Arrows"}
]

# Creating instances of Avenger class for each superhero
avengers_team = [Avenger(hero["name"], hero["age"], hero["gender"], hero["super_power"], hero["weapon"], hero.get("leader", False)) for hero in super_heroes]

# Displaying information about each superhero and checking if they are the leader
for avenger in avengers_team:
    avenger.get_info()
    avenger.is_leader()

# ------------------------------------------
