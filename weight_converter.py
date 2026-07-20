# Weight Converter Application
print("Choose conversion type:\n")
print("1: Kilograms to Pounds")
print("2: Pounds to Kilograms")

choose = input("Choose (1 or 2): ").strip()

if choose == "1":
    kg = float(input("Enter the weight in kilograms: "))
    # Using specific conversion factor
    lbs = kg * 2.20462
    print(f"Weight in pounds: {lbs:.2f}")

elif choose == "2":
    pounds = float(input("Enter the weight in pounds: "))
    kg = pounds * 0.453592
    print(f"Weight in kilograms: {kg:.2f}")

else:
    print("Error: Invalid selection. Please choose 1 or 2.")
