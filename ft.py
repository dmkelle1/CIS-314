import tkinter as tk
from tkinter import messagebox

class WeeklyGoalTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weekly Goal Tracker")

        # Create labels and entries for the goal weight and daily calories
        self.label_goal_weight = tk.Label(root, text="Enter your goal weight (in lbs):")
        self.label_goal_weight.grid(row=0, column=0, padx=10, pady=10)

        # Entry for goal weight (only integers allowed)
        self.entry_goal_weight = tk.Entry(root, width=30)
        self.entry_goal_weight.grid(row=0, column=1, padx=10, pady=10)

         # Create label and entry for current weight
        self.label_current_weight = tk.Label(root, text="Enter your current weight (in lbs):")
        self.label_current_weight.grid(row=1, column=0, padx=10, pady=10)

        # Entry for current weight (only integers allowed)
        self.entry_current_weight = tk.Entry(root, width=30)
        self.entry_current_weight.grid(row=1, column=1, padx=10, pady=10)

        # Days of the week
        self.days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # Create a list to hold the entry widgets for calories
        self.entries_calories = []

        # Create labels and entry boxes for each day of the week
        for idx, day in enumerate(self.days_of_week):
            day_label = tk.Label(root, text=day)
            day_label.grid(row=idx+1, column=0, padx=10, pady=5, sticky="e")

            entry = tk.Entry(root, width=30)
            entry.grid(row=idx+1, column=1, padx=10, pady=5)
            self.entries_calories.append(entry)  # Add the entry widget to the list

        # Create a button to submit the data
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_data)
        self.submit_button.grid(row=8, column=0, columnspan=2, pady=10)

        # Create a Text widget to display the results
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        # Validation function for integers
        self.vcmd = root.register(self.validate_integer)  # Register the validation function

    def validate_integer(self, P):
        """Validate that the input is either an empty string or a valid integer."""
        if P == "" or P.isdigit():  # Allows empty string or digits only
            return True
        else:
            return False

    def submit_data(self):
        """Process the entered goal weight and daily calories."""
        # Get the goal weight
        goal_weight = self.entry_goal_weight.get()

        if not goal_weight.isdigit():
            messagebox.showerror("Input Error", "Please enter a valid goal weight.")
            return

        goal_weight = int(goal_weight)

        # Get the calories for each day
        weekly_calories = []
        for idx, day in enumerate(self.days_of_week):
            calories = self.entries_calories[idx].get()

            if not calories.isdigit():  # Ensure calories input is a valid integer
                messagebox.showerror("Input Error", f"Please enter a valid number of calories for {day}.")
                return

            weekly_calories.append(int(calories))

        # Display the entered data in the result text area
        self.result_text.delete(1.0, tk.END)  # Clear previous results
        self.result_text.insert(tk.END, f"Goal Weight: {goal_weight} kg\n\n")
        self.result_text.insert(tk.END, "Calories consumed per day:\n")

        for idx, day in enumerate(self.days_of_week):
            self.result_text.insert(tk.END, f"{day}: {weekly_calories[idx]} calories\n")

        self.result_text.insert(tk.END, "\nWeekly Summary:\n")
        total_calories = sum(weekly_calories)
        self.result_text.insert(tk.END, f"Total Calories Consumed: {total_calories}\n")

        # You could add a comparison with the goal weight or other logic here as needed

# Create the main window
root = tk.Tk()

# Instantiate the app class
app = WeeklyGoalTrackerApp(root)

# Run the application
root.mainloop()