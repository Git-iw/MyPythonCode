# Password generator:

import random

characters = "!£$%^&*()_-=+{}[]~#@':;?/>.<,|qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

lengthofPassword = int(input("Enter the length of the password: "))

password = ''

for i in range(lengthofPassword):
    password+= random.choice(characters)

print(f"Password: {password}")
