# Range Finder:

numsInput = input("Enter the numbers: ")
numbers = numsInput.split(",")


miniNum = min(int(number) for number in numbers)
maxNum = max(int(number) for number in numbers)
range = maxNum - miniNum

print(f"Range: {range}")
