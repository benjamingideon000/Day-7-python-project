# calculator.py

def calculator():
    # Ask the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask the user for an operator
    operator = input("Enter the operator (+, -, *, /, %, **): ")

    # Calculate and print the result
    if operator == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    elif operator == "%":
        if num2 != 0:
            result = num1 % num2
            print(f"{num1} % {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    elif operator == "**":
        result = num1 ** num2
        print(f"{num1} ** {num2} = {result}")
    else:
        print("Error: Invalid operator.")

if __name__ == "__main__":
    calculator()
