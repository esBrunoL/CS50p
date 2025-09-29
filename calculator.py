#Function are defifed before they are called
#Simple calculator using functions and a while loop

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

#While loop to keep the calculator running until the user decides to exit
selector = ""
while selector != "c":

# Defined data type for the inputs
    x = float(input("Enter a value for x : "))
    y = float(input("Enter a value for y : "))

    selector = input("Choose operation (+, -, *, /):\nPress c to exit. ")

# Conditional statements to perform the selected operation
    if selector == "+":
        print(f"The sum is {add(x, y)}")
    elif selector == "-":
        print(f"The difference is {subtract(x, y)}")
    elif selector == "*":
        print(f"The product is {multiply(x, y)}")
    elif selector == "/":
        print(f"The quotient is {divide(x, y):,}")
    elif selector == "c":
        print("Exiting the calculator.")
    else:
        print("Invalid operation.")