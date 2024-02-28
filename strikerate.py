def strikeRate(balls, runs):
    try:
        strike_rate = float((runs/balls) * 100)
        return strike_rate
    except:
        print("Em rayalo thelidha neeku!")


runsInput = int(input("Runs Scored: "))
ballsInput = int(input("Balls Survived: "))
print(strikeRate(ballsInput, runsInput))
