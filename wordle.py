"""
Amanda Guest - 20147153
28-March-2025
"""

def score_guess(guess, target):
    score = (0,0,0,0,0)
    if guess == target:
        score = (2,2,2,2,2)
        return score
    else:
        return score

guess = "world"
target = "world"

print(score_guess(guess, target))
# Returns (2, 2, 2, 2, 2)