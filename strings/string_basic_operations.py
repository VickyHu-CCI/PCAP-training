ord('a')
chr(97)
#muptiple lines of string '''
test_string = '''line 1
Line 2
Line 3'''
print(len(test_string)) #20

#operator overloading
# + operator
a = 'hello'
b = 'world'
print(a + b) #helloworld
# * operator
print(a * 3) #hellohellohello
# in operator
print('h' in a) #True
print('z' in a) #False
# not in operator
print('h' not in a) #False
print('z' not in a) #True
# string slicing
a = 'hello world'
print(a[0:5]) #hello
print(a[6:]) #world
print(a[:5]) #hello
print(a[-5:]) #world
print(a[-5:-1]) #worl
print(a[::2]) #hlowrd #extract every second character, starting from the first character.
print(a[::-1]) #dlrow olleh

min('i love travelling') # return the caracter with the lowest ASCII value
max('i love travelling') # return the caracter with the highest ASCII value