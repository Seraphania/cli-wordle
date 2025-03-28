# Amanda Guest - 20147153
# 28-March-2025


# Pseudocode: score each letter
#
# for guess_letter in guess
#   if guess_letter in target # Use find (will return the first index)
#       increment score by 1
#
#   if the index value from find matches the current guess_letter index
#       increment score by 1


def score_guess(guess, target):
    score = (0,0,0,0,0)
    if guess == target:
        score = (2,2,2,2,2)
        return score
    else:
        return score

guess = "world"
target = "hello"

print(score_guess(guess, target))
# Returns (0, 0, 0, 0, 0)