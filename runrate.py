import sys

try:
    runsInput = int(input("Runs Scored: "))
    oversInput = int(input("Overs done: "))
    runRate = float(runsInput/oversInput)
    print(f"Run Rate: {runRate}")
except:
    sys.exit("Invalid Input.")
