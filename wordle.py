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
    """
    Scoring algorithm to determine how correct the guess word is

    Arguments
    ---------
    guess = the player's guess word
    target = the target word for the player to guess

    Returns
    -------
    The function should outputs three numbers(0,1,2).
    Each number corresponds to how correct the letter of the guess word compared to the target.
    2 = Correct
    1 = Not in position
    0 = Wrong letter

    Examples
    --------
    Example#1:

    guess_word = "holel"
    target_word = "hello"

    score_guess(guess_word, target_word)

    print(score)

    Expected results: [2,1,2,1,1]

    Example#2:
    guess_word = "hello"
    target_word = "worlds"

    score_guess(guess_word, target_word)

    print(score)

    Expected results: Error: Incorrect word length!

    """

    index = 0
    score = []
    
    if len(target) != len(guess):
        return "Error: Incorrect word length!"
    
    else:
        for char in guess:
            if char is target[index]:
                score.append(2)
            elif char in target:
                score.append(1)
            else:
                score.append(0)

            index += 1

        return score

# TODO: Read File Into Word List Function
def read_words_from_file(filename):
    """
    Reads data from a file, line by line, then stores it on a list.

    Argument
    --------
    filename = the name of the file.
    If the file is inside a folder, the filename should be:
    folder_name/filename.txt

    Returns
    -------
    Outputs a list of words that are already stripped of white lines.
    
    Example
    --------
    example_file_name = project_folder/example.txt

    example_word_list = read_words_from_file(example_file_name)

    print(example_word_list)

    """
    
    word_list = []
    file = open(filename, "r")

    for line in file:
        word_list.append(line.strip())

    file.close()

    return word_list

# TODO: Display Greeting Function
def show_greeting():
    print("+---------- Semi-Wordle ----------+")
    print("|                                 |")
    print("|       Welcome to Wordle!        |")
    print("|                                 |")
    print("+---------------------------------+")

# TODO: Display Instructions Function
def show_instructions():
    print("Instructions")

# TODO: Any Optional Additional Functions
def random_word(words_list):
    """
    Picks a random word from the given list.

    Argument
    --------
    words_list =  list of words that is read from a file

    Returns
    -------
    Outputs a single word that is randomly picked.
    
    Example
    --------
    sample_list = [apple, banana, strawberry, cheese]

    example_word = random_word(sample_list)

    print(example_word)

    Expected output: /Any of the fruit or cheese on the list/
    """
    import random

    target_word = random.choice(words_list)

    return target_word

def display_score(score, guess):
    """
    Displays the score of the guess attempt.

    Argument
    --------
    score = the score got from the score_guess function
    guess = word guess by the player using user input

    Returns
    -------
    Prints out the score and the guess of the player.
    Instead of showing 0,1,2, it is replaced with characters for readability:
    0 = -
    1 = ?
    2 = O
    
    Example
    --------
    score = [1,1,2,2,0]
    guess_word = "world"

    display_score(score, guess_word)

    Expected Results:
     ? ? O O -
     W O R L D
    """
    
    # TODO: Set score output equal to ""
    score_output = ""
    # TODO: Set word output to ""
    word_output = ""

    # TODO: Build score output
    #            Eg, (1,1,0,2,2) should become "? ? - O O"
    for num in score:
        if num == 0:
            score_output += " -"
        elif num == 1:
            score_output += " ?"
        elif num ==2:
            score_output += " O"

    # TODO: Build word output based on guess word
    #            Eg, "rival" should become "R I V A L"
    caps_guess = guess.upper()

    for char in caps_guess:
        word_output += f" {char}"

    # TODO: Display score output
    print(score_output)
    # TODO: Display word output
    print(word_output)

    
# TODO: Play Game Function
def play_game():
    print("Program Starting!") #Changed from Play Game

#TODO: Testing Function
def test_game():
    print ("Test Game")
##    # Test Case 1
##    ##Arrange
##    guess_word = "hello"
##    target_word = "train"
##
##    ##Act
##    score = score_guess(guess_word, target_word)
##
##    ##Assert
##    print("Score:", score, "Expected:", [0, 0, 0, 0, 0])
##
##    # Text Case 2
##    ##Arrange
##    guess_word = "hello"
##    target_word = "hello"
##
##    ##Act
##    score = score_guess(guess_word, target_word)
##
##    ##Assert
##    print("Score:", score, "Expected:", [2, 2, 2, 2, 2])
##
##    # Text Case 3
##    ##Arrange
##    guess_word = "word"
##    target_word = "hello"
##
##    ##Act
##    score = score_guess(guess_word, target_word)
##
##    ##Assert
##    print("Score:", score, "Expected:", [2, 2, 2, 2, 2])

##    # Text Case 4
##    ##Arrange
##    all_word_filename = "resources/all_words.txt"
##
##    ##Act
##    all_word_list = read_words_from_file(all_word_filename)
##
##    ##Assert
##    print("Got:", all_word_list[:5], "Expected:",  ['aahed', 'aalii', 'aargh', 'aarti', 'abaca'])
##
##    # Test Case 5
##    # TODO: Set up your arrange-act-assert test case.
##    ##Arrange
##    target_words_filename = "resources/target_words.txt"
##
##    ##Act
##    target_words_list = read_words_from_file(target_words_filename)
##
##    # Create the statement to show the last 5 words and check that they are correct
##    ##Assert
##    print("Got:", target_words_list[-5:], "Expected:",  ['young', 'youth', 'zebra', 'zesty', 'zonal'])
##
##     # Test Case 6
##    ##Arrange
##    target_words_filename = "resources/target_words.txt"
##    target_words_list = read_words_from_file(target_words_filename)
##    random_words_list = []
##
##    ##Act
##    for count in range(3):
##        random_words_list.append(random_word(target_words_list))
##
##    # Create the statement to show the last 5 words and check that they are correct
##    ##Assert
##    print(random_words_list)

##     # Test Case 7
##    ##Arrange
##    score = [1,0,1,1,2,2,0,2]
##    guess_word = "terrific"
##
##    ##Act
##    display_score(score, guess_word)
##
##    ##Assert
##    print("Expected: \n ? - ? ? O O - O \n T E R R I F I C")

#TODO: Main Program
if DEBUG:
    test_game()
else:
    play_game()

show_greeting()
