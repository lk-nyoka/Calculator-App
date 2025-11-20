# Creating a basic/simple calculator using Python

# Addition function
def add(x, y): 
  return x + y 

# Subtraction function 
def subtract(x, y): 
  return x - y
  
# Multiplication function 
def multiply(x, y): 
  return x * y

# Division function 
def divide(x, y):
  return x / y  


# What user will see first 
print("Hello, please select operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


# Taking input from user, working out the calculation and displaying solution
while True: 
  choice = input("Enter choice(1/2/3/4): ")
  
  if choice in ('1', '2', '3', '4'): 
    try: 
      num1 = float(input("Enter your first number: "))
      num2 = float(input("Enter your second number: "))
      
    except ValueError: 
      print("Invalid input. Please enter a number.")
      continue
    
    if choice == '1': 
      print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2': 
      print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3': 
      print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4': 
      if (num2 == 0):
        print("You cannot divide with zero. Undefined.")
      else: 
        print(num1, "/", num2, "=", divide(num1, num2))
    
    #Checking if use wants to try another calculation
    next_calculation = input("Try another calculation? (yes/no): ")
    if next_calculation.lower() == "no": 
      break 
  else: 
    print("Invalid Input")
      