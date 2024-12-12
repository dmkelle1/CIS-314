import random
winningNumbers = 13
numberRoll = random.randint(1, 100)
print("your number is " + str(numberRoll))
if numberRoll == winningNumbers:
    print("YOU WIN!!!")
else:
    print("you lose")