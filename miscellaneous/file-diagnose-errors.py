from os import strerror

try:
    stream = open('nonexistent.txt')
    stream.close()
except Exception as e:
    print(f"An error occurred: {e}") # An error occurred: [Errno 2] No such file or directory: 'nonexistent.txt'


try:
    stream = open('nonexistent.txt')
    stream.close()
except Exception as e:
    print(e.errno) # 2

try:
    stream = open('nonexistent.txt')
    stream.close()
except Exception as e:
    print(strerror(e.errno)) # No such file or directory
