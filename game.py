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
elif myInput == computerInput:
    print("Sorry, same option was given by me!")
elif myInput == "scissors" and computerInput == "rock":
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
    print("Invalid Option Given")

