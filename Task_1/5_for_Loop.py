# ------------------------------------------
# Task: FOR LOOP
# ------------------------------------------

import random

# ------------------------------------------
# Task 1: Simulate Rolling a Six-Sided Die
# ------------------------------------------

def roll_die_simulation(num_rolls):
    print("Starting Die Roll Simulation...")
    # Initialize counters
    count_6 = 0
    count_1 = 0
    count_double_sixes = 0
    prev_roll = None

    # Roll the die multiple times
    for _ in range(num_rolls):
        roll = random.randint(1, 6)
        
        if roll == 6:
            count_6 += 1
        if roll == 1:
            count_1 += 1
        if prev_roll == 6 and roll == 6:
            count_double_sixes += 1

        prev_roll = roll

    # Print the statistics
    print(f"Times rolled a 6: {count_6}")
    print(f"Times rolled a 1: {count_1}")
    print(f"Times rolled two 6s in a row: {count_double_sixes}")
    print("------------------------------------------")

# ------------------------------------------
# Task 2: Jumping Jacks Workout Routine
# ------------------------------------------

def jumping_jacks_workout():
    print("Starting Jumping Jacks Workout Routine...")
    total_jumping_jacks = 100
    completed_jumping_jacks = 0

    while completed_jumping_jacks < total_jumping_jacks:
        # Perform 10 jumping jacks at a time
        completed_jumping_jacks += 10
        print(f"Performed {completed_jumping_jacks} jumping jacks.")

        if completed_jumping_jacks >= total_jumping_jacks:
            print("Congratulations! You completed the workout.")
            break
        
        # Ask if tired
        tired = input("Are you tired? (yes/no): ").strip().lower()
        
        if tired in ['yes', 'y']:
            # Ask if want to skip remaining sets
            skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
            if skip in ['yes', 'y']:
                print(f"You completed a total of {completed_jumping_jacks} jumping jacks.")
                break
        else:
            # Display remaining jumping jacks
            remaining_jumping_jacks = total_jumping_jacks - completed_jumping_jacks
            print(f"{remaining_jumping_jacks} jumping jacks remaining.")
            print("------------------------------------------")

# ------------------------------------------
# Main Program to Execute Both Tasks
# ------------------------------------------

def main():
    print("------------------------------------------")
    print("Starting Task 1: Rolling a Six-Sided Die")
    roll_die_simulation(20)  # Simulate 20 rolls of a six-sided die
    
    print("------------------------------------------")
    print("Starting Task 2: Jumping Jacks Workout")
    jumping_jacks_workout()  # Start the workout routine

    print("------------------------------------------")
    print("All tasks completed!")
    print("------------------------------------------")

# Run the main function
main()
