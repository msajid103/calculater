# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main function to take user input and perform calculations
def calculator():
    while True:
        print("Options:")
        print("Enter '+' for addition")
        print("Enter '-' for subtraction")
        print("Enter '*' for multiplication")
        print("Enter '/' for division")
        print("Enter 'exist' to end the program")

        user_input = input("Enter: ")

        if user_input == "exist":
            break
        elif user_input in ("+", "-", "*", "/"):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "+":
                print("Result:", add(num1, num2))
            elif user_input == "-":
                print("Result:", subtract(num1, num2))
            elif user_input == "*":
                print("Result:", multiply(num1, num2))
            elif user_input == "/":
                print("Result:", divide(num1, num2))
        else:
            print("Invalid input")

calculator()
