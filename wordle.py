"""
Implementation of the game "Wordle"
Designed to run in a CLI environment
"""
# Amanda Guest - 20147153
# 28-March-2025

import random

def instructions():
    """ print game rules for user """

    rules = '''\
    *** Welcome to CLI Wordle! ***
    Try to guess a 5 letter word in 6 tries...\n
    If a letter is in the correct position it will be marked with an X
    If a letter is in the word, but not in the correct position, it will be marked with an O
    If a letter is not in the word; it will be marked with an _
    _________________
    EXAMPLE:
    Target: P R I Z E
    Guess:  P E T A L
    Score:  X O _ _ _
    '''
    print(rules)
    input("Press enter to continue... ")

def get_target():
    """ get a random word from target-words.txt """
    with open("./resources/target-words.txt", "r") as target_list:
        target_words = []
        for line in target_list:
            target_words.append(line.strip())
        target = str.lower(random.choice(target_words))
        return target

def valid_words():
    """ get a list of all valid words from all-words.txt """
    with open("./resources/all-words.txt", "r") as all_words:
        valid_words = []
        for line in all_words:
            valid_words.append(line.strip())
    return valid_words

def get_guess():
    """ try to get a user guess
        check guess validity: length, valid word, 'help'
        once conditions are met return valid guess
    """
    while True:
        guess = str.lower(input("Please guess a 5-letter word\nOr type \"help\" to review the instructions\nGuess: "))
        if guess == "help":
            instructions()
        elif len(guess) != len(target):
            print(f"\"{guess.upper()}\" is {len(guess)} letters long, your guess should be {len(target)} letters long.")
        elif guess not in valid_words():
            print(f"\"{guess.upper()}\" is not a valid word")
        else: 
            return guess
        
def raw_score(guess, target):
    """ Score guess by letter:
        +1 to score for a letter in GUESS being in TARGET,
        +1 for the letter being in the correct location.
    """
    score = [0,0,0,0,0]
    for i in range(len(guess)):
        letter_score = target.find(guess[i])
        if letter_score >= 0:
            score[i] += 1
            if guess[i] == target[i]:
                score[i] += 1
    return tuple(score) # Just for DevRaf!

def format_score(score):
    """ render the scor is a user-readable format """
    display_score = []
    for i in score:
        if i == 0:
            display_score.append("_")
        elif i == 1:
            display_score.append("O")
        else:
            display_score.append("X")
    return tuple(display_score)

def guess_list_format(guess):
    """ display all guesses in a nice format """
    formatted = ' '
    formatted += ' '.join(guess.upper()) + '\n'
    guess_list.append(formatted)
    for guess in guess_list:
        print(guess, end='\r')

# Game Loop
instructions()
target = get_target()
# print(f"Target: {target.upper()}") ### Leave here for debugging
guess_list = []
for guess_count in range(1,7):
    guess = get_guess() 
    score = format_score(raw_score(guess, target))
    if raw_score(guess, target) == (2,2,2,2,2):
        print("Congratulations! you guessed the word!")
        guess_list_format(guess)
        print("",*score)
        exit()
    else:
        guess_list_format(guess)
        print("",*score)
        print(f"You have {6 - guess_count} guesses remaining.")
        guess_count += 1        
print(f"Sorry, you have used all your guesses, '\n'The word was {target.upper()} '\n'Thanks for playing!")
exit()