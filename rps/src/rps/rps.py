#Rock Paper Scissors Game
#by Joey Williams, Dylan Kelley, and Chase Bowers.
#This program asks the user to pick rock, paper, or scissors and then picks rock, paper, or scissors itself at random to play a game of rock, paper, scissors.
#The program also prints out the score and win rate percentage of your games.
#The goals of this project were to use the random module, input, while and for loops, and if statements to create a virtual game of rock, paper, scissors.
import random
#Function for inputing a players choice of rock, paper, or scissors. Made by Dylan Kelley.
def gameInput():
    userInput = input("Choose R, P, or S, or press E to stop the game")
    return userInput

#Function for running the game rock, paper, scissors. Made by Joseph Williams, Chase Bowers, and Dylan Kelley.
def game():
    playerScore = 0 #Variable for the players score.
    botScore = 0 #Variable for the bots score.
    totalGames = 0 #Variable for number of games played.
    while True: #While loop to keep the game running until you press e. Made by Dylan Kelley
        input = gameInput()
        if ((input == "e") or (input == "E")):
            break # 
        
        playerInputValue = 0 #Variable for the players input.
        printPlayerInput = "" #Variable used to print players input.
        printBotInput = "" #Variable used to print bots input.
        botInputValue = random.randrange(1,4) #Variable for the bots input, randomly generated.

        #Key: 1 is rock, 2 is paper, 3 is scissors.

        #Setting a value for comparison based on input and a string value for printing results. Made by Joey Williams.
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
        #Setting a string value for printing results for botInput. Made by Joey Williams
        if(botInputValue == 1):
            printBotInput = "Rock"
        elif(botInputValue == 2):
            printBotInput = "Paper"
        elif(botInputValue == 3): 
            printBotInput = "Scissors"
        else:
            print("Random range is messed up.")
        
        #Comparison and game itself. Made by Joey Williams.
        if(botInputValue == playerInputValue): #if bot and player get the same thing
            print("Bot chose", printBotInput, "and you chose", printPlayerInput, ", a tie!")
        
        elif(botInputValue == 1): #if bot gets rock
            if(playerInputValue == 2): #and player chooses paper
                print("Bot chose", printBotInput, "and you chose", printPlayerInput, ", you win!") 
                playerScore += 1
                totalGames += 1
            else: #and player chooses scissors
                print("Bot chose", printBotInput, "and you chose", printPlayerInput, ", you lose :(")
                botScore += 1
                totalGames += 1

        elif(botInputValue == 2): #if bot gets paper
            if(playerInputValue == 3): #and player chooses scissors
                print("Bot chose", printBotInput, "and you chose", printPlayerInput, ", you win!") 
                playerScore += 1
                totalGames += 1
            else: #and player chooses rock
                print("Bot chose", printBotInput, "and you chose", printPlayerInput, ", you lose :(")
                botScore += 1
                totalGames += 1

        elif(botInputValue == 3): #if bot gets scissors
            if(playerInputValue == 1): #and player chooses rock
                print("Bot chose", printBotInput, "and you chose", printPlayerInput, ", you win!") 
                playerScore += 1
                totalGames += 1
            else: #and player chooses paper
                print("Bot chose", printBotInput, "and you chose", printPlayerInput, ", you lose :(")
                botScore += 1
                totalGames += 1
        else:
            print("Something went wrong in comparison.") #Else to know if something goes wrong in this part when I was testing it. Joey Williams.
    print("Thank you for playing")
    print("Final Score - Player: %d Bot: %d" % (playerScore, botScore)) #Prints score of the game. Made by Chase Bowers.
    gameStats(playerScore, totalGames)

#Function for determining winrate. Made by Chase Bowers.
def gameStats(input1, input2):
    winRate = (input1 / input2) * 100
    print("Your win rate is", winRate, "%")



game() #Runs the game.