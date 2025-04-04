"""
Implementation of the game "Wordle"
Designed to run in a CLI environment
"""
# Amanda Guest - 20147153
# 28-March-2025

import random

def instructions():
    """Print the game rules"""

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
    """Get a random word from target-words.txt"""
    with open("./resources/target-words.txt", "r") as target_list:
        target_words = []
        for line in target_list:
            target_words.append(line.strip())
        target = str.lower(random.choice(target_words))
        return target

def valid_words():
    """Get a list of all valid words"""
    with open("./resources/all-words.txt", "r") as all_words:
        valid_words = []
        for line in all_words:
            valid_words.append(line.strip())
    return valid_words

def get_guess():
    """get a user guess"""
    guess = str.lower(input("Please guess a 5-letter word\nOr type \"help\" to review the instructions\nGuess: "))
    guess_validate(guess)
    return guess

def guess_validate(guess):
    """Check the guess is the correct length and is a word"""
    if guess == "help":
        instructions()
        get_guess()
        return None
    elif len(guess) != len(target):
        print(f"\"{guess}\" is {len(guess)} letters long, your guess should be {len(target)} letters long.")
        get_guess()
        return None
    elif guess not in valid_words():
        print("That is not a valid word, please try again")
        get_guess()
        return None
    else:
        return guess
    
def raw_score(guess, target):
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

def format_score(score):
    score_display = []
    for i in score:
        if i == 0:
            score_display.append("_")
        elif i == 1:
            score_display.append("O")
        else:
            score_display.append("X")
    return tuple(score_display)

def guess_list_format(guess):
    formatted = ' '
    formatted += ' '.join(guess.upper()) + '\n'
    guess_list.append(formatted)
    for guess in guess_list:
        print(guess, end='')

instructions()
target = get_target()
print(f"Target: {target}")
guess_count = 6
guess_list = []
while guess_count > 0:
    guess = get_guess()
    score = format_score(raw_score(guess, target))
    if raw_score(guess, target) == (2,2,2,2,2):
        print("Congratulations! you guessed the word!")
        guess_list_format(guess)
        print("",*score)
        exit()
    else:
        guess_count -= 1
        guess_list_format(guess)
        print("",*score)
        print(f"You have {guess_count} guesses remaining.\n")               
print(f"Sorry, you didn't guess the word '\n'The word was {target.upper} '\n'Thanks for playing!")
exit()


# TODO #9
# End the game when the player wins or when all valid attempts are complete.

# TODO #10
# Present a completion message to the user.

# TODO #12
"""Please guess a 5-letter word
Or type "help" to review the instructions
Guess: guess
 H E L P S
 G U E S S
 _ O _ O O
You have 4 guesses remaining.

Please guess a 5-letter word
Or type "help" to review the instructions
Guess: sd
"sd" is 2 letters long, your guess should be 5 letters long.
Please guess a 5-letter word
Or type "help" to review the instructions
Guess: catty
 H E L P S
 G U E S S
 S D
 X _ _ _ _
You have 3 guesses remaining.

Please guess a 5-letter word
Or type "help" to review the instructions"""