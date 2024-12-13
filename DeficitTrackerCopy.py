import tkinter as tk
from tkinter import messagebox
# Imports tkinter and messagebox

class CalorieDeficitTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Calorie Deficit Tracker")

        # Creates labels and Entry widgets for current weight, goal weight, and how many months to reach it
        self.CurrentWeightLabel = tk.Label(root, text="Enter your current weight (in lbs):")
        self.CurrentWeightLabel.grid(row=0, column=0, padx=10, pady=10)

        self.CurrentWeightEntry = tk.Entry(root, width=30)
        self.CurrentWeightEntry.grid(row=0, column=1, padx=10, pady=10)

        self.GoalWeightLabel = tk.Label(root, text="Enter your goal weight (in lbs):")
        self.GoalWeightLabel.grid(row=1, column=0, padx=10, pady=10)

        self.GoalWeightEntry = tk.Entry(root, width=30)
        self.GoalWeightEntry.grid(row=1, column=1, padx=10, pady=10)

        self.MonthsLabel = tk.Label(root, text="Enter the number of months to reach your goal:")
        self.MonthsLabel.grid(row=2, column=0, padx=10, pady=10)

        self.MonthsEntry = tk.Entry(root, width=30)
        self.MonthsEntry.grid(row=2, column=1, padx=10, pady=10)

        # Creates a submit button to submit your data
        self.SubmitButton = tk.Button(root, text="Submit", command=self.submitData)
        self.SubmitButton.grid(row=3, column=0, columnspan=2, pady=20)

        # Creates a text box to display your results
        self.ResultText = tk.Text(root, height=6, width=50)
        self.ResultText.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def submitData(self):
        # Gets the entries
        CurrentWeight = self.CurrentWeightEntry.get()
        GoalWeight = self.GoalWeightEntry.get()
        Months = self.MonthsEntry.get()

        # Makes sure inputs are valid and makes them integers
        if not CurrentWeight.isdigit():
            messagebox.showerror("Input Error", "Please enter a valid number.")
            return
        if not GoalWeight.isdigit():
            messagebox.showerror("Input Error", "Please enter a valid number.")
            return
        if not Months.isdigit():
            messagebox.showerror("Input Error", "Please enter a valid number.")
            return

        # Converts to inputs to integers
        CurrentWeight = int(CurrentWeight) # Convert to integer
        GoalWeight = int(GoalWeight) # Convert to integer
        Months = int(Months) # Convert to integer

        # Calculate the Calorie Deficit and checks if the current and goal weight are the same or lower
        WeightLoss = CurrentWeight - GoalWeight
        if WeightLoss <= 0:
            self.ResultText.delete(1.0, tk.END)
            self.ResultText.insert(tk.END, "Your current weight is already the same or below your goal weight.")
            return

        CalorieDeficit = WeightLoss * 3500  # Total calorie deficit (3500 calories per 1 lb)
        TotalDays = Months * 30  # This is assuming every month is 30 days

        # Calculates the daily caloriedeficit
        DailyCalorieDeficit = CalorieDeficit / TotalDays

        # Display entered data and results and calorie deficit
        self.ResultText.delete(1.0, tk.END)  # Clear previous results
        self.ResultText.insert(tk.END, f"Current Weight: {CurrentWeight} lbs\n")
        self.ResultText.insert(tk.END, f"Goal Weight: {GoalWeight} lbs\n")
        self.ResultText.insert(tk.END, f"Number of Months: {Months} months\n\n")
        self.ResultText.insert(tk.END, f"To reach your goal, you need a daily calorie deficit of approximately:")
        self.ResultText.insert(tk.END, f"{DailyCalorieDeficit:.2f} calories per day.\n")

# Creates the main window
root = tk.Tk()

# Instantiate the app class
DeficitTracker = CalorieDeficitTracker(root)

# Run the application
root.mainloop()