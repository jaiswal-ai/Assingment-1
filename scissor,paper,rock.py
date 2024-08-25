import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

def create_interface():
    window = tk.Tk()
    window.title("Rock-Paper-Scissors")

    tk.Label(window, text="Choose your option:", font=("Arial", 14)).pack(pady=20)

    choices_frame = tk.Frame(window)
    choices_frame.pack()

    rock_button = tk.Button(choices_frame, text="Rock", font=("Arial", 14), width=10, command=lambda: play_game('rock'))
    rock_button.grid(row=0, column=0, padx=10)

    paper_button = tk.Button(choices_frame, text="Paper", font=("Arial", 14), width=10, command=lambda: play_game('paper'))
    paper_button.grid(row=0, column=1, padx=10)

    scissors_button = tk.Button(choices_frame, text="Scissors", font=("Arial", 14), width=10, command=lambda: play_game('scissors'))
    scissors_button.grid(row=0, column=2, padx=10)

    window.mainloop()

if __name__ == "__main__":
    create_interface()
