# INSTRUCTIONS:
# Easy-to-play game against a computer. 
# You set the upper and lower limit, 
# the computer holds a number within those bounds, 
# and you have to guess the number.

import random

def guess(x, y):
    random_number = random.randint(x, y)
    while True:
        try:
            guess = int(input(f"Guess a number between {x} and {y}: "))
        except ValueError:
            print("Not a number. Please try again.")
            continue
        if x <= guess <= y:
            if guess < random_number:
                print("Sorry, guess again. Too low.")
                continue
            elif guess > random_number:
                print("Sorry, guess again. Too high.")
                continue
            else:
                print(f"Yay, congrats! You have guessed the number {random_number} correctly.")
                break
        else:
            print(f"Invalid range, please enter a number between {x} and {y}.")
            continue


print("Welcome to this easy-to-play game against a computer.\
    \nYou set the upper and lower limit,\
    \nthe computer holds a number within those bounds,\
    \nand you have to guess the number.\
    \nLet's get right into it!\n")
print("Hi there, what's your name?")
name = input()
print(f"Okay, {name}! Let's establish the range.")
lower_limit = int(input("Set your lower limit: "))
upper_limit = int(input("Set your upper limit: "))
while lower_limit == upper_limit or lower_limit > upper_limit:
    print("Please enter an upper limit greater than your lower limit.")
    upper_limit = int(input("Set your upper limit: "))
guess(lower_limit, upper_limit)