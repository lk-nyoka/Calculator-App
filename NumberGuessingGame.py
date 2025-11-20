import tkinter as tk 
import random 

# We are going to build a number guessing game.
# The computer will randomly generate a number and the user must try and get this number. 
# User has seven chances to get this number. 
# With every input the computer will let the user know if their number is HIGH or LOW

def start_game(): 
    global number, attempts_left
    attempts_left = 7
    number = random.randint(int(low_entry.get()), int(high_entry.get()))
    
    result_label.config(text=f"Game Started! Guess a number between {low_entry.get()} and {high_entry.get()}.")
    guess_entry.config(state="normal")
    guess_button.config(state="normal")
    play_again_button.config(state="disabled")
    
def check_guess(): 
    global attempts_left
    
    try: 
        guess = int(guess_entry.get())
    except ValueError: 
        result_label.config(text="Please enter a valid NUMBER.")
        return
    
    attempts_left -= 1
    
    if guess == number: 
        result_label.config(text=f"CORRECT! The number was {number}.")
        guess_button.config(state="disabled")
        play_again_button.config(state="normal")
    
    elif attempts_left == 0 and guess != number: 
        result_label.config(text=f"GAME OVER! The number was {number}.") 
        guess_button.config(state="disabled")
        play_again_button.config(state="normal")
    
    elif guess > number: 
        result_label.config(text=f"Too HIGH! Attempts left: {attempts_left}")
    else: 
        result_label.config(text=f"Too LOW! Attempts left: {attempts_left}")
        
    guess_entry.delete(0, tk.END)


def reset_game(): 
    result_label.config(text="Enter your range and click START.")
    guess_entry.config(state="disabled")
    guess_button.config(state="disabled")
    play_again_button.config(state="disabled")


root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x350")
root.config(bg="#fff8dc")

title_label = tk.Label(root, text="Number Guessing Game", font=("Arial", 16, "bold"), bg="#fff8dc")
title_label.pack(pady=10)

range_frame = tk.Frame(root, bg="#fff8dc")
range_frame.pack()

tk.Label(range_frame, text="Lower Bound" , bg="#fff8dc").grid(row=0, column=0)
low_entry = tk.Entry(range_frame)
low_entry.grid(row=0, column=1)

tk.Label(range_frame, text="Upper Bound" , bg="#fff8dc").grid(row=1, column=0)
high_entry = tk.Entry(range_frame)
high_entry.grid(row=1, column=1)

start_button = tk.Button(root, text="Start Game", command=start_game, bg="green", fg="white")
start_button.pack(pady=10)

guess_entry = tk.Entry(root, state="disabled")
guess_entry.pack(pady=5)

guess_button = tk.Button(root, text="Guess", command=check_guess, state="disabled", bg="blue", fg="white")
guess_button.pack(pady=5)

result_label = tk.Label(root, text="Enter your range and click START.", bg="#fff8dc")
result_label.pack(pady=10)

play_again_button = tk.Button(root, text="Play Again", command=reset_game, state="disabled", bg="red", fg="white")
play_again_button.pack(pady=10)

root.mainloop()
