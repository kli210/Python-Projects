# INSTRUCTIONS:
# Easy-to-play game against a computer. 
# You and the computer choose between Rock, Paper, and Scissors,
# and on the count of three, 
# both players' choice are simultaneously revealed.
# Rock beats Scissors, Paper beats Rock, and Scissors beat Paper.
# Let the games begin!

import random

def play():
    repeat = False
    while True:
        try:
            if repeat:
                break
            user_action= input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors.\n")
            computer_action = random.choice(['r', 'p', 's'])
            user_action.isalpha()
            if user_action.lower() not in ['r', 'p', 's']:
                print("Please type 'r' for rock, 'p' for paper, 's' for scissors.")
                continue
        except:
            print("Please enter a letter. Type 'r' for rock, 'p' for paper, 's' for scissors.")
            continue
        print(f"\n1..2..3!\nYou chose {user_action}, the computer chose {computer_action}.")
        # r > s, s > p, p > r.
        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "r":
            if computer_action == "s":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_action == "p":
            if computer_action == "r":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cut paper! You lose.")
        elif user_action == "s":
            if computer_action == "p":
                print("Scissors cut paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
    
        while True:
            play_again = input("\nPlay again? (y/n): ")
            if play_again.lower() == "y":
                print("Nice!")
                break
            elif play_again.lower() == "n":
                print("\nGood game! See you again.\n")
                repeat = True
                break
            else:
                print("Please type 'y' for yes, or 'n' for no.")
                continue
        



print("Welcome to this easy-to-play game against a computer.\
    \nYou and the computer choose between Rock, Paper, and Scissors,\
    \nand on the count of three,\
    \nboth players' choice are simultaneously revealed.\
    \nRock beats Scissors, Paper beats Rock, and Scissors beat Paper.\
    \nLet the games begin!'\n")
print("Hi there, what's your name?")
name = input()
print(f"Okay, {name}!")

play()