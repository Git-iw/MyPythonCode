def main():
    numsList = [1,5,2,3,3,4]
    print(numsList)
    duplicateNumber = findDuplicate(numsList)
    print(f"Duplicate Number: {duplicateNumber}")

def findDuplicate(list):
    list.sort()
    # Linear Search
    for i in range(len(list)):
        if list[i] == list[i-1]:
            return list[i]


if __name__ == "__main__":
    main()