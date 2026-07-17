# Shopping Cart Program
# This program allows users to add items and their prices to a cart

cart = []  # Initialize an empty list to store products

while True:
    # Get item name and price from the user
    item = input("What item you want? ")
    price = float(input("What is the price? "))
    
    # Add the item and price as a tuple to the cart list
    cart.append((item, price))
    print(f"{item} has been added to your cart.")
    
    # Ask the user if they want to continue shopping
    choice = input("Do you need any another item? (yes/no): ").strip().lower()
    
    if choice == "yes":
        continue  # Return to the beginning of the loop
    else:
        # Ask if the user wants to view the cart before exiting
        view = input("Do you want to see your items now? (yes/no): ").strip().lower()
        if view == "yes":
            print("Your cart:", cart)
        
        print("Goodbye!")
        break  # Exit the loop and end the program



 
