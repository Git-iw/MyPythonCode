# Simplest RPS game in Python:
# when the option of you and computer is the same, it might scold you.... Sorry!

import random

gameOptions = ["rock","paper","scissors"]

myInput = input("Enter Your Option: ")
myInput = myInput.lower()
computerInput = random.choice(gameOptions)

if myInput == "rock" and computerInput == "scissors":
    print(f"My Option: {computerInput}")
    print("You Win!!")
elif myInput == "scisssors" and computerInput == "rock":
    print(f"My Option: {computerInput}")
    print("I Win!!")
elif myInput == "paper" and computerInput == "rock":
    print(f"My Option: {computerInput}")
    print("You Win!!")
elif myInput == "rock" and computerInput == "paper":
    print(f"My Option: {computerInput}")
    print("I Win!!")
elif myInput == "scissors" and computerInput == "paper":
    print(f"My Option: {computerInput}")
    print("You Win!!")
elif myInput == "paper" and computerInput == "scissors":
    print(f"My Option: {computerInput}")
    print("I Win!!")
else:
    print("Unnayi ray be cheppesh.")

