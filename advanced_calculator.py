# ============================================================
# Script Name : Professional CLI Calculator
# Description : Performs basic arithmetic with full input
#               validation and a repeat loop.
# Author      : Mohammed Hussin
# ============================================================


def calculate(num1, num2, operation):
    """Pure logic: takes two numbers and an operator, returns a result
    or an error string. Does no printing — so it can be reused anywhere."""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/" or operation == "%":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2 if operation == "/" else num1 % num2
    else:
        return "Error: Invalid operation selected."


def get_number(prompt):
    """Keeps asking until the user types a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def calculator():
    """Handles all interaction: input, output, and the repeat loop."""
    print("--- Welcome to the Professional Calculator ---")

    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        operation = input("Select an operation (+, -, *, /, %): ").strip()

        result = calculate(num1, num2, operation)

        # If the result is a number, format it. If it's an error string, show as-is.
        if isinstance(result, str):
            print(result)
        else:
            print(f"The result of {num1} {operation} {num2} is: {result:.2f}")

        again = input("\nDo you want another calculation? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    calculator()
