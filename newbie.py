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

letters_guessed = []


print('Welcome to Hangman! (Press "0" to exit)')

print(letter_marks)

# Main game loop - keep running until player wins or loses
while True:

    # Get a letter guess from the player
    guess = input("Make a Guess, NOW: ")

    if guess == "0":
        break

    if guess in letters_guessed:
        print("Already guessed. Choose another letter.")
        print()
        print()
        continue


    if guess == initial_word:
        print("You guessed the word!!")
        break

    letters_guessed.append(guess)

    # Check if the guessed letter is in the word
    in_word = False

    for i in range(num_letters):
        if guess == initial_word[i]:
            letter_marks[i] = guess
            in_word = True
    
 # Display current progress
    print(letter_marks)

    # If letter is not in word, lose a life
    if not in_word:
        lives -=1
        print("Lives remaining:", lives)


    print(letters_guessed)

    # Check if player is out of lives
    if lives == 0:
        print("YOU LOSE")
        print(initial_word)
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
        
    print()
    print()