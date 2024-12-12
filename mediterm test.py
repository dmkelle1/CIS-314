import random

def gameInput():
    return input("Choose R, P, or S or press E to quit: ").strip()

def game():
    playerScore = 0
    botScore = 0
    
    while True:
        user_input = gameInput()
        print(f"Debug: User input is '{user_input}'")  # Debug print

        if user_input.lower() == "e":
            break  # Exits the game if you press E

        # Check player input
        if user_input.lower() == "r":
            playerInputValue = 1
        elif user_input.lower() == "p":
            playerInputValue = 2
        elif user_input.lower() == "s":
            playerInputValue = 3
        else:
            print("Invalid input. Please choose R, P, S, or E.")
            continue  # Restart the loop if input is invalid

        # Bot choice
        botInputValue = random.randint(1, 3)
        print(f"Debug: Bot chose {['Rock', 'Paper', 'Scissors'][botInputValue - 1]}")  # Display bot choice

        # Game logic
        if botInputValue == playerInputValue:
            print("It's a tie!")
        elif (botInputValue == 1 and playerInputValue == 2) or \
             (botInputValue == 2 and playerInputValue == 3) or \
             (botInputValue == 3 and playerInputValue == 1):
            print("You win!")
            playerScore += 1
        else:
            print("You lose!")
            botScore += 1

    print("Thanks for playing!")
    print(f"Final Score -> You: {playerScore}, Bot: {botScore}")

if __name__ == "__main__":
    game()