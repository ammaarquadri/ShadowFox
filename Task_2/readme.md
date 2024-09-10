# Web Scraper & Hangman Game Project

## Overview
This project includes two tasks: a **Web Scraper** and a **Hangman Game**, both implemented in Python. The Web Scraper is designed to extract data from websites, while the Hangman Game is a word-guessing game with hints and visual feedback.

---

## 1. Web Scraper

### Description
The Web Scraper extracts specific data from web pages using Python's `BeautifulSoup` library. For practice, the scraper is configured to extract data from the ShadowFox website. This data can be stored and analyzed for further use.

### Features
- **Data Extraction**: Utilizes `BeautifulSoup` to parse HTML and extract desired information.
- **ShadowFox Integration**: Extracts sample data from ShadowFox website for practice.
- **Data Storage**: Scraped data is saved in appropriate formats (e.g., CSV, JSON) for easy retrieval.
- **Error Handling**: Implements mechanisms to handle common scraping issues like missing elements, timeouts, or HTTP errors.

### Workflow
1. **Scraping the Web**: Uses `requests` to fetch the web page and `BeautifulSoup` to parse the HTML.
2. **Data Extraction**: Extracts relevant information from the page (e.g., titles, links, text).
3. **Data Storage**: Saves the scraped data into a structured file format.
4. **Error Handling**: Logs errors or skips problematic pages to ensure the scraper runs smoothly.

### Requirements
- Python 3.x
- `requests` library
- `BeautifulSoup4` library

### Usage
1. Install the necessary libraries:
   ```bash
   pip install requests beautifulsoup4
   ```
2. Run the scraper:
   ```bash
   python scraper.py
   ```

---

## 2. Hangman Game

### Description
The Hangman game is a command-line word-guessing game where the player tries to guess a hidden word. The game provides visual feedback in the form of a Hangman figure and offers hints to the player.

### Features
- **Random Word Selection**: A word is randomly chosen from a predefined list.
- **Text-Based Interface**: Displays the Hangman figure and the partially revealed word.
- **User Input Validation**: Ensures valid input from the user (single letter only).
- **Win/Loss Conditions**: Tracks incorrect guesses and determines when the game is over.
- **Hints**: Provides hints to help the player guess the word.
- **Play Again Option**: Once the game ends, players can choose to start a new game.

### Workflow
1. **Game Setup**: Initializes the chosen word, guessed letters, incorrect guesses, and allowed attempts.
2. **Game Loop**: Continuously prompts the player for guesses until they win or lose.
3. **Visual Progress**: Updates the interface to show the Hangman figure and partially guessed word.
4. **Win/Loss Check**: Tracks the player’s progress and determines if they’ve won or lost.
5. **Play Again**: Offers a play-again option at the end of each game.

### Requirements
- Python 3.x

### Usage
1. Run the game:
   ```bash
   python hangman.py
   ```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/web-scraper-hangman.git
   ```
2. Navigate to the project directory:
   ```bash
   cd web-scraper-hangman
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## Contributing
Feel free to fork this repository and submit pull requests if you have any improvements or fixes.

---

## Acknowledgements
Special thanks to the ShadowFox team for providing a platform to practice web scraping.

---
