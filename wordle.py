"""
Implementation of the game "Wordle"
Designed to run in a CLI environment
"""
# Amanda Guest - 20147153
# 28-March-2025

# Senior Developer feedback:

#     Combine the "get_target()" and "valid_words()" functions into a single read-file function.

# Additional "nice to have" Senior Dev feedback:

#     Improve modularity so that words of any length can be used, avoiding magic numbers.
#     Avoid the use of exit() statements.
#     Make the game loop a function.


# Client feedback:

#     Improve readability by adding line breaks after the score is displayed.
#     Add the ability to play again.
#     Save the number of attempts to a file.
#     When a game is won, show the number of attempts made, as well as the average number of attempts.

import random

all_words = "all-words.txt"
target_words = "target-words.txt"

def instructions():
    """
    Print the game rules for the user.
    """

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

def read_wordlist(word_type):
    """
    Read wordlist files and return contents as a list
    """
    path = "./resources/"
    with open(path,word_type, "r") as file:
        words = []
        for line in file:
            words.append(line.strip())
    return words

def get_target(target_list):
    """
    Choose a random target word.
    """
    target = str.lower(random.choice(target_words))
    return target

def get_guess(valid_words):
    """
    Try to get a user guess;
    Check guess validity: length, valid word, 'help'
    Once the conditions are met return valid guess.
    """
    while True:
        guess = str.lower(input("Please guess a 5-letter word\nOr type \"help\" to review the instructions\nGuess: "))
        if guess == "help":
            instructions()
        elif len(guess) != len(target):
            print(f"\"{guess.upper()}\" is {len(guess)} letters long, your guess should be {len(target)} letters long.")
        elif guess not in get_valid_words():
            print(f"\"{guess.upper()}\" is not a valid word")
        else: 
            return guess
   
def calculate_raw_score(guess, target):
    """
    Score guess by letter:
    Letters in the correct location = 2
    Letters in that are in the target but in the worng location = 1
    Letters that appear in the guess more times than they appear in target = 0
    Letters in guess that are not in target = 0    
    """
    score = [0,0,0,0,0]
    for i in range(len(guess)):
        if guess[i] == target[i]:
            score[i] = 2
            target = target[:i] + '*' + target[i+1:]
            guess = guess[:i] + '*' + guess[i+1:]
    for i in range(len(guess)):
        if guess[i] == '*':
            score[i] = 2
        elif guess[:i+1].count(guess[i]) > target.count(guess[i]):
            score[i] = 0
        elif target.find(guess[i]) >=0:
            score[i] = 1
        else:
            score[i] = 0

    return tuple(score) # Just for DevRaf!

def format_score(score):
    """
    Render the score in a user-readable format
    """
    display_score = []
    for i in score:
        if i == 0:
            display_score.append("_")
        elif i == 1:
            display_score.append("O")
        else:
            display_score.append("X")
    return tuple(display_score)

def format_guess_list(guess):
    """
    Render all guesses in a user-readable format
    """
    formatted = ' '
    formatted += ' '.join(guess.upper()) + '\n'
    guess_list.append(formatted)
    for guess in guess_list:
        print(guess, end='\r')

def game_loop():
    instructions()
    valid_words = read_wordlist(all_words)
    target_words = read_wordlist(target_words)
    target = str.lower(random.choice(target_words))
    # print(f"Target: {target.upper()}") ### Leave here for debugging
    guess_list = []
    for guess_count in range(1,7):
        guess = get_guess()
        score = format_score(calculate_raw_score(guess, target))
        if calculate_raw_score(guess, target) == (2,2,2,2,2):
            print("Congratulations! you guessed the word!")
            format_guess_list(guess)
            print("",*score)
            input("Press enter to exit... ")
            exit()
        else:
            format_guess_list(guess)
            print("",*score)
            print(f"You have {6 - guess_count} guesses remaining.")
            guess_count += 1        
    print(f"Sorry, you have used all your guesses, '\n'The word was {target.upper()} '\n'Thanks for playing!")
    input("Press enter to exit... ")
    exit()
