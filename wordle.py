"""
Implementation of the game "Wordle"
Designed to run in a CLI environment
"""
# Amanda Guest - 20147153
# 28-March-2025

import random

def instructions():
    """Define game rules"""

    rules = '''\
    *** Welcome to CLI Wordle! ***
    Try to guess a 5 letter word in 6 tries...\n
    If a letter is in the correct position it will be marked with an X
    If a letter is in the word, but not in the correct position, it will be marked with a O
    If a letter is not in the word; it will be marked with a _
    _________________
    EXAMPLE:
    Target: P R I Z E
    Guess:  P E T A L
    Score:  X O _ _ _
    '''
    print(rules)
    input("Press enter to begin... ")

def get_target():
    """get a random word from target.txt"""
    with open("./resources/target-words.txt", "r") as target_list:
        target_words = []
        for line in target_list:
            target_words.append(line.strip())
        target = str.upper(random.choice(target_words))
        return target

def score_guess(guess, target):
    """Score guesses by letter, 
        +1 to score for a letter in GUESS being in TAGET,
        +1 for the letter being in the correct location."""
    score = [0,0,0,0,0]
    for i in range(len(guess)):
        letter_score = target.find(guess[i])
        if letter_score >= 0:
            score[i] += 1
            if guess[i] == target[i]:
                score[i] += 1
    return tuple(score) # Just for DevRaf!

# TODO #4
# Use a sequential algorithm to read a list of valid words and a separate list of target words.


# TODO #6
def get_guess():
    guess = str.upper(input("Please guess a 5-letter word\nOr type \"help\" to review the instructions\nGuess: "))
    return guess

# TODO #7
# Check if the guess that is entered is a valid guess.
# Case insensitivity!



# TODO #9
# End the game when the player wins or when all valid attempts are complete.

instructions()
target = get_target()
print(f"Target: {target}") # Delete this line later!
print(get_guess())

# TODO #10
# Present a completion message to the user.

