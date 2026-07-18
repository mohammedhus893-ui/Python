import math

# Assigning Pi value from math library
pi = math.pi

# Greeting message
print("Welcome to the Circle Circumference Calculator")

# Getting user input and converting it to float
radius = float(input("Enter the radius of the circle: "))

# Calculating the circumference
circumference = 2 * pi * radius

# Displaying the exact result
print(f"The exact circumference is: {circumference}")

# Asking the user for the preferred rounding method
rounding_choice = input("Would you like to round the result up to the nearest whole number (enter 'yes'), or use standard rounding (enter 'no')? ").strip().lower()

# Executing the chosen rounding method
if rounding_choice == "yes": 
    # Rounding up (Ceiling)
    print(f"Result (rounded up): {math.ceil(circumference)}")
elif rounding_choice == "no":
    # Standard rounding
    print(f"Result (standard round): {round(circumference)}")
else:
    # Handling invalid input
    print("Invalid choice, displaying the exact value instead.")
    print(f"Result: {circumference}")


