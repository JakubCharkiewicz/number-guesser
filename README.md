## Number Guesser Game
This Python project is a simple command-line number guessing game where the player tries to guess a randomly chosen number between 1 and 100. It also features some ASCII art that is displayed during the game.

## Features
1. Awesome Donut Art: The game includes an option to display some fun donut ASCII art.

2. Number Guesser Game: The main game is a number guessing game where the player must guess the correct number within a set number of attempts.
The player can choose between two difficulty levels:
   - Easy: 10 attempts to guess the number.
   - Hard: 5 attempts to guess the number.
3. Input Validation: The game checks for valid numerical inputs and ensures proper handling of errors.
## How to Play
- Clone or download the repository.
  - Make sure you have the art module installed. You can install it using:
  - pip install art
  - Run the number-guessing-game.py file.

A menu will appear with the following options:

Awesome Donut: Displays some cool ASCII art.
Number Guesser Game: Starts the game.
Exit: Exits the game.
If you choose to play the game, select a difficulty level:

Easy: You get 10 attempts to guess the number.
Hard: You get 5 attempts to guess the number.
The game will tell you if your guess is too high or too low until you either guess correctly or run out of attempts.

## Code Structure
- menu(): Displays the main menu and handles the user's selection.
- diff_chooser(): Lets the user choose the difficulty level.
- diff_easy(attempts): Handles the easy difficulty level, giving the player 10 attempts.
- diff_hard(attempts): Handles the hard difficulty level, giving the player 5 attempts.
- ASCII art is printed when specific options are selected.
## Prerequisites
- Python 3.x
- art Python package (for displaying ASCII art)
