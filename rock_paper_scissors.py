''' as taken from Tech with Tim
    but had to code for draws afterwards
'''

import random


user_wins = 0
computer_wins = 0
user_draws = 0

options = ["rock", "paper", "scissors"]
options[0]

while True:
    user_input = input("To play simply type Rock, paper, or scissors \n or Q to quit or S for your score. ").lower()
    if user_input == "q":
        break
    
    if user_input == "s":
        print("You won", user_wins)
        print("The computer won", computer_wins)
        print("You and the computer drew", user_draws)
     
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("The computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "rock" and computer_pick == "rock":
        print("It's a draw!")
        user_draws += 1

    elif user_input == "paper" and computer_pick == "paper":
        print("Nobody won!")
        user_draws += 1

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Your picks match so it is a draw!")
        user_draws += 1
   
    else:
        print("You lose!")
        computer_wins += 1


print("Goodbye!")
