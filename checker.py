# Palindrome Checker

from PyDictionary import PyDictionary

palindromeInput = input("Enter the Word: ")
palindrome = ''

for letter in palindromeInput:
    palindrome = letter + palindrome
    # What is happening above is: as we gave a condition that adds letter plus the empty string,
    # as the new letter comes into the string, it will take the first place.

dictionary = PyDictionary
meaning = dictionary.meaning(palindrome)


if palindrome == palindromeInput:
    print(f"{palindromeInput} is a palindrome.")
    print(f"Meaning: {meaning}")   
else:
    print(f"The given word {palindrome} is not a palindrome")

