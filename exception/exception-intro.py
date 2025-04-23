# The code above is a simple example of exception handling in Python.
try:
    input_value = int(input("Enter an integer: "))
    print(f'The inverse of {input_value} is {1/input_value}')
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")

# If a systax error in the try block occurs, the except block will not be executed.
# The program will terminate with a syntax error.
# Syntax errors are not caught by the try-except block.
try:
    raise SyntaxError("This is a syntax error")
except:
    print("An error occurred. Got it")

try:
    5:4
except:
    print("A new error occurred. Got it")

