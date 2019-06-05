# game.py

import random


print("Rock, Paper,Scissors, Shoot!") # you can also comment to the right

# capture inputs

user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes)")

print("--------------")
print("YOU CHOSE:", user_choice)


# validate inputs

if user_choice not in ["rock", "paper", "scissors"]:
    print("INVALID SELECTION, PLEASE TRY AGAIN")
    exit()


# generate computer selection

print("GENERATING...")

computer_choice = random.choice(["rock", "paper", "scissors"])

print("--------------")
print("COMPUTER CHOICE:", computer_choice)

# determine the winner



# display final outputs / outcomes


