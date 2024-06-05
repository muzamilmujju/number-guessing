import tkinter as tk
import random
from tkinter import Button, Entry, Label, StringVar

win = tk.Tk()
win.geometry("750x750")
win.title("PythonGeeks")

guess = StringVar()
hint = StringVar()
final_score = StringVar()

Entry(win, textvariable=guess, width=3, font=('Ubuntu', 50), relief=tk.GROOVE).place(relx=0.5, rely=0.3, anchor=tk.CENTER)
Entry(win, textvariable=hint, width=50, font=('Courier', 24), relief=tk.GROOVE, bg='orange').place(relx=0.5, rely=0.7, anchor=tk.CENTER)
Entry(win, text=final_score, width=2, font=('Ubuntu', 24), relief=tk.GROOVE).place(relx=0.61, rely=0.85, anchor=tk.CENTER)

Label(win, text='I challenge you to guess the number', font=("Courier", 25)).place(relx=0.5, rely=0.09, anchor=tk.CENTER)

answer = random.randint(1, 10)  # Generate a random number between 1 and 100

attempts = 0

def check_guess():
    global attempts
    user_guess = int(guess.get())

    if user_guess == answer:
        hint.set("Congratulations! You guessed it right.")
    elif user_guess < answer:
        hint.set("Try a higher number.")
    else:
        hint.set("Try a lower number.")

    attempts += 1
    final_score.set(f"Attempts: {attempts}")

    if attempts >= 10:
        hint.set(f"Game over! The correct answer was {answer}.")

Button(win, text="Submit Guess", command=check_guess, font=("Courier", 24)).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

win.mainloop()
