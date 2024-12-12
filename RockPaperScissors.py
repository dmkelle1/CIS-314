import random

def gameInput():
    userInput = input("Choose R, P, or S, or press E to stop the game")
    return userInput

def game():
    playerScore = 0
    botScore = 0
    while True:
        input = gameInput()
        if ((input == "e") or (input == "E")):
            break # Exits the game if you press E
        
        playerInputValue = 0
        printPlayerInput = ""
        printBotInput = ""
        botInputValue = random.randrange(1,4)

        #1 is rock, 2 is paper, 3 is scissors.

        #Setting a value for comparison based on input and a string value for printing results.
        if((input == "r") or (input == "R")):
            playerInputValue = 1
            printPlayerInput = "Rock"
        elif(input == "p") or (input == "P"):
            playerInputValue = 2
            printPlayerInput = "Paper"
        elif(input == "s") or (input == "S"):
            playerInputValue = 3
            printPlayerInput = "Scissors"
        else:
            print("False input.")
            continue
        #Setting a string value for printing results for botInput.
        if(botInputValue == 1):
            printBotInput = "Rock"
        elif(botInputValue == 2):
            printBotInput = "Paper"
        elif(botInputValue == 3): 
            printBotInput = "Scissors"
        else:
            print("Random range is messed up.")
        
        #Comparison and game itself.
        if(botInputValue == playerInputValue): #if bot and player get the same thing
            print("Bot chose", printBotInput, "and you chose", printPlayerInput, ", a tie!")
        
        elif(botInputValue == 1): #if bot gets rock
            if(playerInputValue == 2): #and player chooses paper
                print("Bot chose", printBotInput, "and you chose", printPlayerInput, ", you win!") 
                playerScore += 1
            else: #and player chooses scissors
                print("Bot chose", printBotInput, "and you chose", printPlayerInput, ", you lose :(")
                botScore += 1

        elif(botInputValue == 2): #if bot gets paper
            if(playerInputValue == 3): #and player chooses scissors
                print("Bot chose", printBotInput, "and you chose", printPlayerInput, ", you win!") 
                playerScore += 1
            else: #and player chooses rock
                print("Bot chose", printBotInput, "and you chose", printPlayerInput, ", you lose :(")
                botScore += 1

        elif(botInputValue == 3): #if bot gets scissors
            if(playerInputValue == 1): #and player chooses rock
                print("Bot chose", printBotInput, "and you chose", printPlayerInput, ", you win!") 
                playerScore += 1
            else: #and player chooses paper
                print("Bot chose", printBotInput, "and you chose", printPlayerInput, ", you lose :(")
                botScore += 1
        else:
            print("Something went wrong in comparison.")
    print("Thank you for playing")
    print("Final Score: player: %d Bot: %d" % (playerScore, botScore))
    #gameStats(playerScore, botScore)

#def gameStats(input1, input2):
    #total games played
    #winrate
    #anything else you want to add



game()




    

    


        