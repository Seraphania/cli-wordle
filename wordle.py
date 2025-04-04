"""
Implementation of the game "Wordle"
Designed to run in a CLI environment
"""
# Amanda Guest - 20147153
# 28-March-2025

def score_guess(guess, target):
    """Score guesses by letter, +1 to score for a letter in guess being in the target word, +1 for the letter being in the correct location."""
    score = [0,0,0,0,0]
    for i in range(len(guess)):
        letter_score = target.find(guess[i])
        if letter_score >= 0:
            score[i] += 1
            if guess[i] == target[i]:
                score[i] += 1
                if guess.count(guess[0:i]) > target[0:i].count(guess[i]):
                    score[i] = 0

    return tuple(score) # Just for DevRaf!

guess = "melee"
target = "elect"

print(score_guess(guess, target))
# Output: (2, 2, 2, 2, 2)

