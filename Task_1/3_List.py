# ------------------------------------------
# Task: List
# ------------------------------------------

# Initial list of superheroes
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print("------------------------------------------")

# 1. Calculate the number of members in the Justice League.
num_members = len(justice_league)
print(f"Number of members in the Justice League: {num_members}")
print("------")

# 2. Batman recruited Batgirl and Nightwing as new members. Add them to the list.
justice_league.extend(["Batgirl", "Nightwing"])
print("After adding Batgirl and Nightwing:", justice_league)
print("------")

# 3. Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list.
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After moving Wonder Woman to the beginning:", justice_league)
print("------")

# 4. Move either "Green Lantern" or "Superman" in between Aquaman and Flash.
# Let's choose "Green Lantern" for this task.
justice_league.remove("Green Lantern")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Green Lantern")
print("After moving Green Lantern in between Aquaman and Flash:", justice_league)
print("------")

# 5. Replace the existing list with the new members.
new_members = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
justice_league = new_members
print("After replacing with new members:", justice_league)
print("------")

# 6. Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.
justice_league.sort()
print("After sorting alphabetically:", justice_league)
print("------")

# BONUS: Predict the new leader
new_leader = justice_league[0]
print(f"The new leader is: {new_leader}")

print("------------------------------------------")