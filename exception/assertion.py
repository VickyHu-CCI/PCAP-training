'''
USE assertion:
1. For debugging/testing your code
2. For documenting your code

DO NOT use assertion:
1. For handling runtime errors, handle AssertionError with try-except block
    (e.g. catching exceptions that can occur during normal operation of the program)
2. For checking user input, validating data, or checking preconditions
'''

def calculate_inverse(number):
    assert (number != 0), "Cannot calculate inverse of zero"
    return 1 / number

calculate_inverse(0) # AssertionError: Cannot calculate inverse of zero