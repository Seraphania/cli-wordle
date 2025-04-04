"""
Implementation of the game "Wordle"
Designed to run in a CLI environment
"""
# Amanda Guest - 20147153
# 28-March-2025

# TODO #3
# Present game instructions to player (That is, display an output to the screen).

# TODO #4
# Use a sequential algorithm to read a list of valid words and a separate list of target words.
with open("./resources/target-words.txt", "r") as target_list:
    target = []
    for line in target_list:
        target.append(line.strip())
    print(f"First 5 words of target-words.txt:\n {target[:5]}")
    print(f"Last 5 words of target-words.txt:\n {target[-5 : len(target)]}\n")

with open("./resources/all-words.txt", "r") as all_list:
    all_words = []
    for line in all_list:
        all_words.append(line.strip())
    print(f"First 5 words of all-words.txt:\n {all_words[:5]}")
    print(f"Last 5 words of all-words.txt:\n {all_words[-5 : len(all_words)]}")


# TODO #5
# Select a word at random from the list of target words using a library function (refer to the developer briefing for the exact syntax).

# TODO #6
# Prompt the user to enter a guess.
guess = "melee"

# TODO #7
# Check if the guess that is entered is a valid guess.

# TODO #8
# Score the guess by providing clues on each character’s match to the target word’s characters.
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

print(score_guess(guess, target))


# TODO #9
# End the game when the player wins or when all valid attempts are complete.

# TODO #10
# Present a completion message to the user.










