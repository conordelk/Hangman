# Import word list and random number generator
from words import WORDS
import random

# Initialize number of lives
lives = 6

# Pick a random word from the word list
initial_word = WORDS[random.randint(0,len(WORDS)-1)]

# Count how many letters are in the word
num_letters = len(initial_word)

# Create a list to show guessed letters, start with underscores
letter_marks = ["_"] * num_letters


print("Welcome to Hangman!")

# Main game loop - keep running until player wins or loses
while True:

    # Get a letter guess from the player
    guess = input("Make a Guess, NOW: ")

    # Check if the guessed letter is in the word
    in_word = False

    for i in range(num_letters):
        if guess == initial_word[i]:
            letter_marks[i] = guess
            in_word = True
    
    # If letter is not in word, lose a life
    if not in_word:
        lives -=1

    # Check if player is out of lives
    if lives == 0:
        print("YOU LOSE")
        break

    # Check if all letters have been guessed
    all_letters = True

    for letter in letter_marks:
        if letter == "_":
            all_letters = False

    # If all letters are revealed, player wins
    if all_letters == True:
        print("YOU WIN!!!")
        break
        
    # Display current progress
    print(letter_marks)