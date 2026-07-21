"""
Photon Energy Calculator
Calculates the energy of a photon based on its frequency using Planck's constant.
"""

def calculate_photon_energy():
    # Planck's constant (J.s) defined as a constant
    PLANCK_CONSTANT = 6.626e-34

    print("--- Photon Energy Calculator ---")
    
    try:
        # Requesting input from the user
        frequency = float(input("Enter the frequency of the photon (in Hz): "))
        
        # Validating input logic
        if frequency < 0:
            print("Error: Frequency cannot be negative.")
        else:
            # Calculating energy
            energy = PLANCK_CONSTANT * frequency
            
            # Displaying result in scientific notation (standard for physics)
            print(f"The energy of the photon is: {energy:.3e} Joules")
            
    except ValueError:
        # Handling non-numeric input
        print("Error: Invalid input! Please enter a numerical value for the frequency.")

if __name__ == "__main__":
    calculate_photon_energy()