# Amanda Guest - 20147153
# 28-March-2025

def score_guess(guess, target):
    score = [0,0,0,0,0]
    for i in range(len(guess)):
        print(f"guess: {guess[i]}, target: {target[i]}")
        letter_score = target.find(guess[i])
        if letter_score >= 0:
            score[i] += 1
            if guess[i] == target[i]:
                score[i] += 1
    return tuple(score) # Just for DevRaf!

guess = "world"
target = "world"

print(score_guess(guess, target))
