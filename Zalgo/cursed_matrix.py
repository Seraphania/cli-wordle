import random
import time
import os
import sys

# Make sure the terminal can handle UTF-8 nightmares
sys.stdout.reconfigure(encoding='utf-8')

# ANSI escape for bright green
GREEN = "\033[1;32m"
RESET = "\033[0m"

# Zalgo diacritics
UP = [chr(i) for i in range(0x0300, 0x036F)]
DOWN = [chr(i) for i in range(0x036F, 0x0374)]

def zalgo_char(char, madness=5):
    """Returns a single character with Zalgo diacritics"""
    return char + ''.join(random.choices(UP + DOWN, k=madness))

def cursed_matrix(cols=80, speed=0.05, zalgo_chance=0.1):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    os.system('cls' if os.name == 'nt' else 'clear')
    print(GREEN, end='')

    try:
        while True:
            line = ''
            for _ in range(cols):
                c = random.choice(chars + '                  ')  # Add space to reduce solid wall effect
                if random.random() < zalgo_chance:
                    c = zalgo_char(c, madness=random.randint(1, 4))
                line += c
            print(line)
            time.sleep(speed)
    except KeyboardInterrupt:
        print(RESET)
        print("\nMatrix-Zalgo stream terminated. Sanity partially restored.")

if __name__ == '__main__':
    cursed_matrix(100, 0.5, .1)