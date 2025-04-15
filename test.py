keyboard = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def display_keyboard(keyboard):
    """
    print letters
    """
    for letter  in keyboard:
        print(letter.upper(), end=' ') 

# display_keyboard(keyboard)

print('\u001b[49mHello World\u001b[0m')