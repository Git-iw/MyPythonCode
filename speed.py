import sys

def main():
    try:
        distance = float(input("Enter the Distance covered: "))
        time = float(input("Enter the Time taken: "))
        speed = speedCalculator(distance, time)
        print(f"{speed}")
    except:
        sys.exit("Maths chaduvukoledha?")

def speedCalculator(distance, time):
    speed = float(distance/time)
    return speed

if __name__ == "__main__":
    main()