# The else block is executed if the try block does not raise an exception.
# The else block is useful for code that should run only if the try block was successful.
# The else block is optional and can be omitted if not needed.
try:
    value = int(input('Enter a number: '))
    print(1/value)
except:
    print('Something went wrong.')
else:
    print('Everthing is perfect')

# finally block is always executed no matter an exception was raised or not.
finally:
    print('This is the end of the program.')
# The finally block is usually used for database connections, file operations, or cleanup actions.