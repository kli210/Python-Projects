import random

def play():
    while True:
        user_action= input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors.\n")
        computer_action = random.choice(['r', 'p', 's'])
        print(f"\nYou chose {user_action}, the computer chose {computer_action}")
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
        
        play_again = input("\nPlay again? (y/n): ")
        if play_again.lower() != "y":
            print("\nGood game! See you again.\n")
            break
        else:
            print("Nice!")

play()