# INSTRUCTIONS:
# Easy-to-play game against a computer. 
# You set the upper and lower limit, 
# and hold a number within those bounds,
# the computer guesses your number.

import random

def computer_guess(x, y):
    low = x
    high = y
    feedback = ''
    correct_input = True
    while True:
        try:
            if correct_input:
                if low > high:
                    print("Out of bounds. There's no more number left for me to guess.. Try again.")
                    break
                guess = random.randint(low, high)
                correct_input = False
            feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)?")
            feedback.isalpha()
            if feedback not in ['h', 'l', 'c']:
                print('Please type "h" for too high, "l" for too low, or "c" for correct.')
                continue
        except:
            print('Please enter a letter. Type "h" for too high, "l" for too low, or "c" for correct.')
            continue
        correct_input = True
        if feedback != 'c':
            if feedback == 'h':
                high = guess - 1
                if low == high:
                    guess = low  # or high since low = high.
                    break
                continue
            elif feedback == 'l':
                low = guess + 1
                if low == high:
                    guess = low  # or high since low = high.
                    break
                continue
        elif feedback == 'c':
            break
    if low == high or low < high:
        print(f"Yay! I've guessed your number, {guess}, correctly!")

print("Welcome to this easy-to-play game against a computer.\
    \nYou set the upper and lower limit\
    \nand hold a number within those bounds,\
    \nthe computer guesses your number.\
    \nLet's jump right into it!\n")
print("Hi there, what's your name?")
name = input()
print(f"Okay, {name}! Let's establish the range.")
lower_limit = int(input("Set your lower limit: "))
upper_limit = int(input("Set your upper limit: "))
while lower_limit == upper_limit or lower_limit > upper_limit:
    print("Please enter an upper limit greater than your lower limit.")
    upper_limit = int(input("Set your upper limit: "))
print("Choose a number, and I'll take a guess..")
computer_guess(lower_limit, upper_limit)