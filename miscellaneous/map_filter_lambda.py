import re
# lambda function in python is a small anonymous function
# it can take any number of arguments, but can only have one expression
# it is a single line function, so no need to use return statement
# lambda function can be used when you need a nameless function for a short period of time
# lambda function can be used as an argument to higher order functions



#lambda parmater1, parameter2: expression
lambda_add = lambda x, y: x + y
print(lambda_add(2, 3))  # 5

def apply_fun(element, function):
    for i in element:
        print(function(i))

apply_fun([1, 2, 3, 4, 5], lambda x: x**2)  # 1,4,9,16,25
apply_fun([1, 2, 3, 4, 5], lambda x: 1/x)  # 1,0.5,0.3333333333333333,0.25,0.2
apply_fun([1, 2, 3, 4, 5], lambda x: 0)  # 0, 0, 0, 0, 0

# map(function, iterable) 
# map() applies the function to all the items in the iterable

lambda_func = lambda x: x*2
initial_list = [1, 2, 3, 4, 5]
mapped_result = map(lambda_func, initial_list)
print('The mapped list is:')
print(mapped_result)  # <map object at 0x7f7e52d53df0>
# print(next(mapped_result))  # 2
# print(next(mapped_result))  # 4
# print(next(mapped_result))  # 6
# print(next(mapped_result))  # 8
# print(next(mapped_result))  # 10
# print(next(mapped_result))  # StopIteration

# for element in mapped_result:
#     print(element, end=',')  # 2,4,6,8,10,

print(list(mapped_result))  # [2, 4, 6, 8, 10]

print(list(map(lambda x: x*2, initial_list)))  # [2, 4, 6, 8, 10]

# filter(function, iterable)
# filter() creates an iterator of elements for which the function returns true

print('The filtered list is:')
print(list(filter(lambda x: x%2 == 0, initial_list)))  # [2, 4]

emails = [
    'john.doe@example.com', 
    'jane.doe@domain.org', 
    'not_an_email', 
    'user123@website.net', 
    'fake_email@', 
    'hello.world@python.com', 
    'invalid-email', 
    'test.user@company.co', 
    'random_string', 
    'admin@server.io'
]
# Regular expression pattern for a valid email address
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# Filter the list of emails using the regex pattern
valid_emails = list(filter(lambda email: re.match(email_pattern, email), emails))
print('The valid emails are:')
print(valid_emails) 
#[
# 'john.doe@example.com', 
# 'jane.doe@domain.org', 
# 'user123@website.net', 
# 'hello.world@python.com', 
# 'test.user@company.co', 
# 'admin@server.io'
#]
