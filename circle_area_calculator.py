import math

# Welcome message to the user
print("Welcome to the Circle Area Calculator")

# Defining Pi constant from the math library
pi = math.pi

# Getting the radius input from the user and converting it to a float
radius = float(input("Enter the radius of the circle: "))

# Calculating the radius squared using pow()
radius_squared = pow(radius, 2)

# Calculating the area of the circle
area = pi * radius_squared

# Displaying the final result with units
print(f"The area of the circle is {area:.2f} cm²")