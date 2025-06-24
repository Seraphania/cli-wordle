"""
Implementation of the game "Wordle"
Designed to run in a CLI environment
"""
# Amanda Guest - 20147153
# 28-March-2025
# for much cooler version made by someone much better, see: word.audino.net
import random

path = "./resources/" # constants should be uppercase
all_words = "all-words.txt"
target_words = "target-words.txt"
stats = "stat-file.txt"
attempts = 6

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
    input("Press enter to continue...\n")

def read_file(path, file_name):
    """
    Read files and return the contents as a list
    """
    with open(path + file_name, "r") as file:
        words = []
        for line in file:
            words.append(line.strip())
    return words

def get_guess(target, valid_words):
    """
    Try to get a user guess;
    Check guess validity: length, valid word, 'help'
    Once the conditions are met return valid guess.
    """
    while True:
        guess = str.lower(input("Please guess a 5-letter word\nOr type \"help\" to review the instructions\n\nGuess: "))
        if guess == "help":
            instructions()
        if guess == "hint":
            print(target)
        elif len(guess) != len(target):
            print(f"\"{guess.upper()}\" is {len(guess)} letters long, your guess should be {len(target)} letters long.")
        elif guess not in valid_words:
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

def display_score(score):
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

def display_results(guess, guess_list, raw_score):
    """
    Render all guesses in a nice user-readable format
    """
    formatted = ' '
    formatted += ' '.join(guess.upper()) + '\n'
    guess_list.append(formatted)
    for guess in guess_list:
        print(guess, end='\r')
    print("",*display_score(raw_score), '\n')

def save_stats(guess_count):
    """
    Save the number of guesses this game to a file
    """
    with open(path + stats, 'a+') as file:
        file.write(str(guess_count))
        file.write('\n') 

def average_stat(): # calculate_average would be a better name
    """
    Retun the average guess count from all games played locally
    rounded to the nearest whole number
    """
    with open (path + stats, 'r') as file:
        stat_list = []
        for line in file:
            stat_list.append(int(line.strip())) # int strips alutomatically don't need strip
    
    average_stat = round(sum(stat_list) / len(stat_list))
    return average_stat

def continue_game(start):
    """
    Verify whether the user would like to continue
    """
    while start not in ("y", "n"):
        start = input("Invalid input. To continue please enter 'y' to exit please enter 'n' ")
    return start

def game_loop():
    """
    Main gameplay loop
    """
    valid_words = read_file(path, all_words)
    targets = read_file(path, target_words)
    target = str.lower(random.choice(targets))
    guess_list = []
    for guess_count in range(1, (attempts + 1)):
        guess = get_guess(target, valid_words)
        raw_score = calculate_raw_score(guess, target)
        if raw_score == (2,2,2,2,2):
            display_results(guess, guess_list, raw_score)
            print("Congratulations! you guessed the word!")
            save_stats(guess_count)
            print(f"You guessed the word in {guess_count} guesses\nThe average number of guesses is {average_stat()}")

            print (f"") # Could be better bit super clear.
            return continue_game(input("Would you like to play again? y/n... "))
        else:
            display_results(guess, guess_list, raw_score)
            print(f"You have {attempts - guess_count} guesses remaining.")
    print(f"Sorry, you have used all your guesses,\nThe word was {target.upper()}\nThanks for playing!")
    save_stats(guess_count)
    print(f"The average number of guesses is {average_stat()}")
    return continue_game(input("Would you like to play again? y/n... "))

instructions()        
while True:
    response = game_loop()
    if response != "y":
        break

input("Thanks for playing CLI-Wordle :)\nPress enter to exit... ")
