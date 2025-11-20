import tkinter as tk 
import math

# We are creating a calculator. This calculator will have buttons showing numbers 0-9 and +,-,x,/ (operation signs). 
# The calculator will also have an equal sign (as a button) and a backspace button. 
# User will press the digits he wants to calculate and the system will read the values and make calculations. 

def start_calculation(): 
    number_one.config(state="normal")
    number_two.config(state="normal")
    number_three.config(state="normal")
    number_four.config(state="normal")
    number_five.config(state="normal")
    number_six.config(state="normal")
    number_seven.config(state="normal")
    number_eight.config(state="normal")
    number_nine.config(state="normal")
    number_zero.config(state="normal")
    plus_sign.config(state="normal")
    minus_sign.config(state="normal")
    multiply_sign.config(state="normal")
    divide_sign.config(state="normal")
    back_space.config(state="disabled")
    equal_sign.config(state="disabled")
    results_label.config(state="normal")
    
def user_entry(value): 
    results_label.insert(tk.END, value) 
    
def calculate(): 
    expression = results_label.get()
    expression = expression.replace("x", "*")

    try: 
        result =  eval(expression)
        results_label.delete(0, tk.END)
        results_label.insert(tk.END, str(result))
    except: 
        results_label.delete(0, tk.END)
        results_label.insert(tk.END, "Error")
        
def delete_last(): 
    current = results_label.get()
    results_label.delete(0, tk.END)
    results_label.insert(0, current[:-1])
    
    
root = tk.Tk()
root.title("Calculator")
root.geometry("700x600")
root.config(bg="white")

title_label = tk.Label(root, text="CALCULATOR", font=("Arial", 16, "bold"), bg="white")
title_label.pack(pady=10)     

button_frame = tk.Frame(root, bg="white")
button_frame.pack()

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

for i in range(4): 
    button_frame.grid_columnconfigure(i, weight=1)
    button_frame.grid_rowconfigure(i, weight=1)

border_frame = tk.Frame(root, bg="black", bd=0)
border_frame.pack()

number_one = tk.Button(button_frame, text="1", command=lambda: user_entry("1"), bg="grey", fg="white", width=8, height=3, font=("Arial", 18))
number_one.grid(row=0, column=0, sticky="nsew")

number_two = tk.Button(button_frame, text="2", command=lambda: user_entry("2"), bg="grey", fg="white", width=8, height=3, font=("Arial", 18))
number_two.grid(row=0, column=1, sticky="nsew")

number_three = tk.Button(button_frame, text="3", command=lambda: user_entry("3"), bg="grey", fg="white", width=8, height=3, font=("Arial", 18))
number_three.grid(row=0, column=2, sticky="nsew")

number_four = tk.Button(button_frame, text="4", command=lambda: user_entry("4"), bg="grey", fg="white", width=8, height=3, font=("Arial", 18))
number_four.grid(row=1, column=0, sticky="nsew")

number_five = tk.Button(button_frame, text="5", command=lambda: user_entry("5"), bg="grey", fg="white", width=8, height=3, font=("Arial", 18))
number_five.grid(row=1, column=1, sticky="nsew")

number_six = tk.Button(button_frame, text="6", command=lambda: user_entry("6"), bg="grey", fg="white", width=8, height=3, font=("Arial", 18))
number_six.grid(row=1, column=2, sticky="nsew")

number_seven = tk.Button(button_frame, text="7", command=lambda: user_entry("7"), bg="grey", fg="white", width=8, height=3, font=("Arial", 18))
number_seven.grid(row=2, column=0, sticky="nsew")

number_eight = tk.Button(button_frame, text="8", command=lambda: user_entry("8"), bg="grey", fg="white", width=8, height=3, font=("Arial", 18))
number_eight.grid(row=2, column=1, sticky="nsew")

number_nine = tk.Button(button_frame, text="9", command=lambda: user_entry("9"), bg="grey", fg="white", width=8, height=3, font=("Arial", 18))
number_nine.grid(row=2, column=2, sticky="nsew")

number_zero = tk.Button(button_frame, text="0", command=lambda: user_entry("0"), bg="grey", fg="white", width=8, height=3, font=("Arial", 18))
number_zero.grid(row=3, column=1, sticky="nsew")

plus_sign = tk.Button(button_frame, text="+", command=lambda: user_entry("+"), bg="grey", fg="white", width=8, height=3, font=("Arial", 18))
plus_sign.grid(row=0, column=3, sticky="nsew")

minus_sign = tk.Button(button_frame, text="-", command=lambda: user_entry("-"), bg="grey", fg="white", width=8, height=3, font=("Arial", 18))
minus_sign.grid(row=1, column=3, sticky="nsew")

multiply_sign = tk.Button(button_frame, text="x", command=lambda: user_entry("x"), bg="grey", fg="white", width=8, height=3, font=("Arial", 18))
multiply_sign.grid(row=2, column=3, sticky="nsew")

divide_sign = tk.Button(button_frame, text="/", command=lambda: user_entry("/"), bg="grey", fg="white", width=8, height=3, font=("Arial", 18))
divide_sign.grid(row=3, column=3, sticky="nsew")

equal_sign = tk.Button(button_frame, text="=", command=calculate, bg="grey", fg="white", width=8, height=3, font=("Arial", 18))
equal_sign.grid(row=3, column=2, sticky="nsew")

back_space = tk.Button(button_frame, text="<", command=delete_last, bg="grey", fg="white", width=8, height=3, font=("Arial", 18))
back_space.grid(row=3, column=0, sticky="nsew")

results_label = tk.Entry(root, state="normal", bg="white", width=30, font=("Arial", 32), justify="right")
results_label.pack(pady=20, ipady=10)

root.mainloop()

