# Average Finder:

numsInput = input("Enter the numbers: ")
numsLength = len(numsInput)

if numsLength >= 2:
    # print("First test valid.")
    numbers = numsInput.split(",")
    lengthofnums = len(numbers)
    addedNums = sum(int(number) for number in numbers)
    average = addedNums/lengthofnums
    print(f"Average: {average}")
else:
    # print("First test failed.")
    print("Invalid length of numbers given.")


