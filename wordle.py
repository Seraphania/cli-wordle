"""
Implementation of the game "Wordle"
Designed to run in a CLI environment
"""
# Amanda Guest - 20147153
# 28-March-2025

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

# Output:
# First 5 words of target-words.txt:
#  ['aback', 'abase', 'abate', 'abbey', 'abbot']
# Last 5 words of target-words.txt:
#  ['young', 'youth', 'zebra', 'zesty', 'zonal']

# First 5 words of all-words.txt:
#  ['aahed', 'aalii', 'aargh', 'aarti', 'abaca']
# Last 5 words of all-words.txt:
#  ['zuzim', 'zygal', 'zygon', 'zymes', 'zymic']


guess = "melee"

# print(score_guess(guess, target))
# Output: (0, 1, 1, 1, 1)

