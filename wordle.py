# Semi-Wordle
#
# Author: Benz Lenard Culanggo
# Student ID: 20156183
#
# Course: Certificate IV Programming
# Lecturer: Para O'Kelly

# TODO:
#Repiclate wordle mechanics using learned programming

# Variables and Constants
# TODO: Define Constants
DEBUG = False
# TODO: Define Variables 

# Application Functions
# TODO: Score Guess Function
def score_guess(guess, target):
    score = []
    for char in target:
        score.append(0)

    return score

# TODO: Read File Into Word List Function

# TODO: Display Greeting Function
def show_greeting():
    print("Welcome")

# TODO: Display Instructions Function
def show_instructions():
    print("Instructions")

# TODO: Any Optional Additional Functions 

# TODO: Play Game Function
def play_game():
    print("Play Game")

#TODO: Testing Function
def test_game():
    print ("Test Game")
    # Test Case 1
    ##Arrange
    guess_word = "hello"
    target_word = "train"

    ##Act
    score = score_guess(guess_word, target_word)

    ##Assert
    print("Score:", score, "Expected:", [0, 0, 0, 0, 0])

#TODO: Main Program
if DEBUG:
    test_game()
else:
    play_game()
