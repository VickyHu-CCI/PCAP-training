def return_bigger(a,b):
    try:
        return a if a > b else b
    except Exception as e:
        print('An unexpected error occurred:', e)
        return None
    
print(return_bigger(5, 10)) # 10
print(return_bigger(5, '10')) # An unexpected error occurred: '>' not supported between instances of 'int' and 'str' None

print('--- BaseException Hierarchy ---')
for subclass in BaseException.__subclasses__():
    print(subclass.__name__)

print('--- Exception Hierarchy ---')
for subclass in Exception.__subclasses__():
    print(subclass.__name__)

# Exception args is typically used to pass some details about why a given exception was raised.
# The args attribute is a tuple that contains the arguments passed to the exception constructor.
# If no arguments were passed, the tuple is empty.
try:
    raise Exception
except Exception as e:
    print(e.args) # ()

try:
    raise Exception('I do not like this')
except Exception as e:
    print(e.args) # ('I do not like this',)

try:
    raise Exception('I do not like this', 'in fact, I hate it')
except Exception as e:
    print(e.args) # ('I do not like this', 'in fact, I hate it')

try:
    1/0
except Exception as e:
    print(e.args)
# ('division by zero',)

try:
    5 < 'a'
except Exception as e:
    print(e.args)
# ('<', 'not supported between instances of \'int\' and \'str\'')

