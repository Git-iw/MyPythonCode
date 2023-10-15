#!/usr/bin/env python

# I used linux for the program development

from fractions import Fraction  

expression = input("Expression: ")
length = len(expression)

try:
    if "+" in expression:
        addition = expression.split("+")
        sum = int(addition[0]) + int(addition[1])
        print(f"Sum: {sum}")
    elif "-" in expression and length < 5:
        subtraction = expression.split("-")
        difference = int(subtraction[0]) - int(subtraction[1])
        print(f"Sum: {difference}")
    elif "*" in expression and "**" not in expression:
        multiplication = expression.split("*")
        product = int(multiplication[0]) * int(multiplication[1])
        print(f"Sum: {product}")
    elif "/" in expression:
        division = expression.split("/")
        quotient = int(division[0]) / int(division[1])
        print(f"Sum: {quotient}")
    elif "**" in expression:
        powerSolving = expression.split("**")
        length = len(powerSolving)
        exponent = int(powerSolving[1])
        if exponent < 0:
            negativeExponent = exponent
            absoluteExponent = abs(exponent)
            powerAns = int(powerSolving[0]) ** absoluteExponent
            Thepower = Fraction(1, powerAns)
            print(f"The Power: {Thepower}")
        else:
            Thepower = int(powerSolving[0]) ** exponent
            print(f"The Power: {Thepower}")
    else:
        print("Invalid Expression.")
except ValueError:
    print("Invalid Expression.")



