import random
import os

def check_in(num):
    while True:
        try:
            num = int(num)
            if 1 <= num <= 32:
                return num
            else:
                num = input("Please enter a whole number from 1-32:\n")
        except ValueError:
            num = (input("Please enter a whole number from 1-32:\n"))

def mess_up(string, madness):

    marks = list(map(chr, range(768, 879)))
    new_string = ""
    words = string.split()
    for word in words:
        new_string += ' '
        for letter in word:
            new_string += letter + "".join(random.choices(marks, k = madness))
    return new_string

def run_loop(inp):
    if inp == "n":
        string = input("What text would you like messed up?:\n")
        madness = check_in(input("On a scale of 1-32, how messed up would you like it to be?\n"))
        os.system('clear')
        os.system('cls')
        print(mess_up(string, madness))
        run_loop(input("Press 'n' to mess up more text, type 'ahhhh' to exit:\n"))
        os.system('clear')
        os.system('cls')
    elif inp == "ahhhh":
        os.system('clear')
        os.system('cls')
        print("Thank you for messing up your text \nH̵͍̳̓̏̾ͤe͉̬̻̳̎̈ͅ C̶̢͎͎͗ͨ̅o̵̷͕̩ͭ͐͒m̵̭̹̻͚̓̈e̘̜̪͙̭͉ͩs̯̝͖ͬ̈͊͟!")
        exit()
    else:
        os.system('clear')
        os.system('cls')
        run_loop(input("would you like to exit? n/ahhhh?:\n"))

print("Welcome to a Silly  Z̜̄̎͗a̩̮̣ͨl͚̳̚͝g̦̭͕̚o̸̶̱ͭ-̨̦̗͋t̶͇̀͠e̗̦̚̚x̧̟̠̅t̛̖͐͠ generator")
run_loop("n")

