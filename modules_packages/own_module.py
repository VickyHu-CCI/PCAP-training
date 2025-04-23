import sys
import os

lib_path = '../lib_path'  # Define the path to the parent directory
sys.path.append(lib_path)  # Add the parent directory to the system path
print(sys.path)  # Print the updated system path
# Now you can import modules from the parent directory

import surfshop


cart = surfshop.ShoppingCart()


if __name__ == "__main__":
    # This code will only run if this file is executed directly
    print("This module is being run directly")
else:
    # This code will run if this file is imported
    print("This module has been imported")
