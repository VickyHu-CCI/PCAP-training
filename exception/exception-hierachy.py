'''
BaseException
    ├── Exception -- SystemExit -- KeyboardInterrupt
        ├── ArithmeticError  ------- LookupError ---------- TypeError --------ValueError
            ├── ZeroDivisionError      ├── IndexError
            ├── OverflowError          ├── KeyError
                      ...         
'''

# example of SystemExit
import sys
user_name = input('Enter your name: ')
if user_name == '':
    print('Empty name. I cannot work with that. I am closing the program. Bye!')
    sys.exit()
print(f'Hello {user_name}. I am glad to meet you.')
print('Let\'s get started...')