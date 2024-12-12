import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        # List of words to choose from
        self.words = ['python', 'java', 'computer', 'programming', 'hangman', 'developer']
        self.word_to_guess = random.choice(self.words)
        self.guessed_word = ['_'] * len(self.word_to_guess)
        self.remaining_attempts = 6
        self.guessed_letters = []

        # Label to display the word with hidden letters
        self.word_label = tk.Label(root, text=' '.join(self.guessed_word), font=('Arial', 24))
        self.word_label.pack(pady=20)

        # Label to display the remaining attempts
        self.attempts_label = tk.Label(root, text=f"Remaining attempts: {self.remaining_attempts}", font=('Arial', 14))
        self.attempts_label.pack(pady=10)

        # Entry box for letter guesses
        self.guess_entry = tk.Entry(root, font=('Arial', 14))
        self.guess_entry.pack(pady=10)
        self.guess_entry.focus()

        # Submit button to make a guess
        self.submit_button = tk.Button(root, text="Guess", font=('Arial', 14), command=self.check_guess)
        self.submit_button.pack(pady=10)

        # Label for displaying guessed letters
        self.guessed_label = tk.Label(root, text="Guessed Letters: ", font=('Arial', 12))
        self.guessed_label.pack(pady=10)

    def check_guess(self):
        """Check the user's guess and update the game state."""
        guess = self.guess_entry.get().lower()
        
        # Check if the input is valid (a single letter)
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            self.guess_entry.delete(0, tk.END)
            return

        # Check if the letter has already been guessed
        if guess in self.guessed_letters:
            messagebox.showwarning("Already Guessed", "You've already guessed this letter.")
            self.guess_entry.delete(0, tk.END)
            return

        # Add the guessed letter to the guessed letters list
        self.guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in self.word_to_guess:
            for index, letter in enumerate(self.word_to_guess):
                if letter == guess:
                    self.guessed_word[index] = guess
            self.update_word_label()
        else:
            self.remaining_attempts -= 1
            self.update_attempts_label()

        # Check if the game is over
        if self.remaining_attempts == 0:
            self.game_over(False)
        elif '_' not in self.guessed_word:
            self.game_over(True)

        # Clear the input field for the next guess
        self.guess_entry.delete(0, tk.END)

    def update_word_label(self):
        """Update the label showing the guessed word with hidden letters."""
        self.word_label.config(text=' '.join(self.guessed_word))

    def update_attempts_label(self):
        """Update the label showing the remaining attempts."""
        self.attempts_label.config(text=f"Remaining attempts: {self.remaining_attempts}")

    def game_over(self, won):
        """Display a message when the game is over (win/lose)."""
        if won:
            messagebox.showinfo("You Win!", "Congratulations! You guessed the word.")
        else:
            messagebox.showinfo("Game Over", f"You lost! The word was '{self.word_to_guess}'.")
        self.root.quit()  # Close the application

# Create the main window
root = tk.Tk()

# Instantiate the Hangman game
game = HangmanGame(root)

# Run the application
root.mainloop()