import re

test_string = 'How anmy\tstings\nwill you see?'
print(test_string) 
# How anmy        stings
# will you see?
print(test_string.split()) #['How', 'anmy', 'stings', 'will', 'you', 'see?']
joined_string = ' '.join(['How', 'anmy', 'stings', 'will', 'you', 'see?']) 
print(joined_string)    # How anmy stings will you see?

name = ['John', 'Doe', 'Adam', 'Babarah']
name_sorted = sorted(name)
print(name_sorted) # ['Adam', 'Babarah', 'Doe', 'John']

name.sort() # sort the list in place
print(name) # ['Adam', 'Babarah', 'Doe', 'John']
# The sorted() function returns a new sorted list from the elements of any iterable.
# The sort() method sorts the original list and returns None.

