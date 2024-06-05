import tkinter as tk
from tkinter import messagebox
import random


secret_number = random.randint(1, 10)

attempts = 0

def check_guess():
    global attempts
    attempts += 1
    player_guess = int(guess_entry.get())

    if player_guess < secret_number:
        hint_label.config(text="Too low! Try again.")
    elif player_guess > secret_number:
        hint_label.config(text="Too high! Try again.")
    else:
        messagebox.showinfo("Congratulations", f"Correct! You guessed it in {attempts} attempts.")
        win.destroy()

win = tk.Tk()
win.title("Number Guessing Game")
win.geometry("400x200")

guess_entry = tk.Entry(win, width=10)
guess_entry.pack(pady=20)


check_button = tk.Button(win, text="Check Guess", command=check_guess)
check_button.pack()


hint_label = tk.Label(win, text="I'm thinking of a number between 1 and 100.")
hint_label.pack()

win.mainloop()
