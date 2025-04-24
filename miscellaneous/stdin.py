# stdin for standard input is equal to input(), by default reads user input from the keyboard not from a file

# stderr for standard error is equal to print()

import sys

for line in sys.stdin:
    if line.rstrip() == 'q':
        break
    print(line, end='-')
print('You pressed q, so I want to quit now. Bye!')

