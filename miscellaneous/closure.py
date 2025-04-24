# A closure is a technique for binding variables to a function without using a class.
# It allows the function to remember the values of the variables even after they have gone out of scope.
# A closure is a function object defined inside another function that remembers the values of the variables of the outer function.
# Closure is used to replace some classes and to create decorators.

def greet(text):
    def print_greeting():
        print(text)
    return print_greeting
# The outer function greet() returns the inner function print_greeting() without calling it.
# The inner function print_greeting() has access to the variable text from the outer function greet().
# When the inner function is called, it prints the value of text.
# text is a free variable in the inner function.
say_hello = greet("Hello, World!")
say_hello()  # Output: Hello, World!
# The closure remembers the value of text even after the outer function has finished executing.
greet('Lovely')() # Output: Lovely

def make_multiplier(x):
    def multiplier(n):
        return x*n
    return multiplier
# The outer function make_multiplier() returns the inner function multiplier() without calling it.
# The inner function multiplier() has access to the variable x from the outer function make_multiplier().
# When the inner function is called, it multiplies the value of n by x.
# x is a free variable in the inner function.
double = make_multiplier(2)
triple = make_multiplier(3)
multiply_12 = make_multiplier(12)
print(double(5))  # Output: 10
print(triple(5))  # Output: 15
print(multiply_12(20))  # Output: 240

