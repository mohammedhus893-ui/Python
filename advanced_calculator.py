def calculator():
    """
    A professional CLI calculator that performs basic arithmetic operations.
    Includes error handling for invalid inputs and division by zero.
    """
    print("--- Welcome to the Professional Calculator ---")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Select an operation (+, -, *, /, %): ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error: Division by zero is not allowed."
        elif operation == "%":
            result = num1 % num2
        else:
            return "Error: Invalid operation selected."

        return f"The result of {num1} {operation} {num2} is: {result:.2f}"

    except ValueError:
        return "Error: Invalid input. Please enter numeric values."

if __name__ == "__main__":
    print(calculator())