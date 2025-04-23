# example long string
test_string = 'ilovetravellingaroundtheworld'

test_string.index('travelling')  # returns 2
my_text = 'this is my sample string'
my_text.index('is')  # returns 2
my_text.find('is')  # returns 2
my_text.index('is', 3)  # returns 5
my_text.find('is', 3)  # returns 5
# my_text.index('are')  # raises ValueError
my_text.find('are')  # returns -1
my_text.find('is',10,15)  # returns -1
# The find() method returns -1 if the substring is not found, 
# while the index() method raises a ValueError.
# The find() method is more flexible and can be used to search for substrings in a string, 
# while the index() method is more strict and will raise an error if the substring is not found.
print('work work work'.find('work')) # 0
print('work work work'.rfind('work')) # 10
print('work work work'.find('work',2)) # 5
print('work work work'.rfind('work',2)) # 10
print('work work work'.find('work',2,5)) # -1
print('work work work'.rfind('work',2,5)) # -1

#isalnum()
# The isalnum() method returns True if all characters in the string are alphanumeric (a-z, A-Z, 0-9) 
# and there is at least one character,
# otherwise it returns False.
#isalpha()
# The isalpha() method returns True if all characters in the string are alphabetic (a-z, A-Z)
# and there is at least one character,
# otherwise it returns False.
#isdigit()
# The isdigit() method returns True if all characters in the string are digits (0-9)
# and there is at least one character,
# otherwise it returns False.
#islower()
# The islower() method returns True if all characters in the string are lowercase (a-z)
#isupper()
# The isupper() method returns True if all characters in the string are uppercase (A-Z)
#isspace()
# The isspace() method returns True if all characters in the string are whitespace (space, tab, newline)