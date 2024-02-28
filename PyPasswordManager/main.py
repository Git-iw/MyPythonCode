# Main file for password manager


# Creating functions for easy code

# View uses for loop in readlines function to get the lines and print them
def view():
    with open("passwords.txt", 'r') as fileofPwdsr:
        for line in fileofPwdsr.readlines():
            print(line) 

# Add uses .write method to write what is given as input
def add():
    accountName = input("Enter account name: ")
    password = input("Enter password: ")
    with open("passwords.txt", 'a') as fileofPwds:
        fileofPwds.write("\n" + accountName + " | " + password + "\n")



# Takes inupt from the user
masterPassword = input("Enter the Master passsword: ")



# Condition for validating Master Password
try:
    if masterPassword == "F;=pwr{']LM,!Z%%/)!*<lDL":
        while True:
            mode = input("Do you want to create a new password or read the existing(add, view, quit): ")
            if mode == "add":
                add()
            elif mode == "view":
                view()
            elif mode == "quit":
                break
    else:
        print("Invalid Master Password")
except:
    print("Yerri Pappa, cheppindhi cheyyi!")
