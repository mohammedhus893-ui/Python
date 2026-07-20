# Temperature Converter Application
print("--- Temperature Converter ---")
print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")

choice = input("Select conversion (1 or 2): ").strip()

try:
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"Result: {celsius}°C is equal to {fahrenheit:.2f}°F")

    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"Result: {fahrenheit}°F is equal to {celsius:.2f}°C")

    else:
        print("Error: Invalid selection. Please choose 1 or 2.")

except ValueError:
    print("Error: Invalid input! Please enter a valid numerical value for the temperature.")