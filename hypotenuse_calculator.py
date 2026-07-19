import math

def calculate_hypotenuse():
    """
    Calculates the hypotenuse of a right-angled triangle 
    using the Pythagorean theorem: c = sqrt(a² + b²)
    """
    try:
        # Get side lengths from the user with descriptive prompts
        side_a = float(input("Enter the length of the adjacent side: "))
        side_b = float(input("Enter the length of the opposite side: "))

        # Calculate the hypotenuse using the math.hypot function for accuracy and efficiency
        hypotenuse = math.hypot(side_a, side_b)

        # Output the result formatted to 2 decimal places
        print(f"The calculated hypotenuse is: {hypotenuse:.2f}")
        
    except ValueError:
        # Handle cases where input is not a valid number
        print("Error: Please enter valid numerical values.")

if __name__ == "__main__":
    calculate_hypotenuse()