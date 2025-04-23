# This program demonstrates exception propagation in Python.
# If a function that raises an exception doesn't have try-except block,
# the exception propagates to the caller function.
# If the caller function doesn't handle the exception, it propagates again 
# until there finally is a try-except block somewhere in the function called stack/chain.
# If there is no try-except block anywhere in the function call stack,
# Python will simply show a nasty error message and terminate the program.

def get_day(user_info:list):
    day = int(input('What is the day of your bday? '))
    user_info.append(day)

def get_month(user_info:list):
    month = int(input('What is the month (1-12) of your bday? '))
    user_info.append(month)

def get_year(user_info:list):
    year = int(input('What is the year of your bday? '))
    user_info.append(year)

def get_birthday(user_info:list):
    try:
        get_day(user_info)
        get_month(user_info)
        get_year(user_info)
        print('Your birthday is:', user_info[0], '/', user_info[1], '/', user_info[2])
    except ValueError as e:
        print('Invalid input. Please enter a number.')
        print(e)
    except Exception as e:
        print('An unexpected error occurred:', e)

print('--- Birthday Program ---')
user_info = []
get_birthday(user_info)

