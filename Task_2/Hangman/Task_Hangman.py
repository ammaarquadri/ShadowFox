import random

# List of words to choose from
word_list = ['python', 'development', 'scraper', 'hangman', 'internship']

def get_hint(word):
    """Return a hint for the word."""
    hints = {
        'python': 'A popular programming language',
        'network': 'System of interconnected computers',
        'scraper': 'Tool for extracting data from websites',
        'hangman': 'A word guessing game',
        'database': 'Organized collection of data',
        'algorithm': 'Step-by-step procedure for solving a problem',
        'repository': 'Storage location for software code',
        'debugging': 'Process of fixing errors in code',
        'internship': 'A professional learning experience'
    }
    return hints.get(word, "No hint available")

def display_progress(word, guessed_letters):
    """Show the current progress of the word."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = random.choice(word_list)  # Randomly select a word
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6

    print(f"Welcome to Hangman! Here's your hint: {get_hint(word)}")

    while incorrect_guesses < max_attempts:
        # Display current progress
        print("\n" + display_progress(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! You have {max_attempts - incorrect_guesses} attempts left.")

        # Check for win condition
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")

    if input("Play again? (y/n): ").lower() == 'y':
        hangman()

# Run the game
hangman()
