class Dog():
    counter = 0
    # Constructor
    def __init__(self, name, age):
        self.__name = name
        self.age = age
        Dog.counter += 1

print(Dog.counter) # 0

my_pet = Dog('Rover', 5)
kates_pet = Dog('Fluffy', 3)
adams_pet = Dog('Fido', 2)

if hasattr(my_pet, 'name'):
    print(f'my_pet\'s name is {my_pet.name}')
else:
    print('my_pet has no name')
# my_pet has no name
# The hasattr() function returns True if the object has the specified attribute,
# otherwise it returns False. It will return False if the attribute is private.

if hasattr(my_pet, 'age'):
    print(f'my_pet\'s age is {my_pet.age}')
else:
    print('my_pet has no age')
# my_pet's age is 5

if hasattr(my_pet, '_Dog__name'):
    print(f'my_pet\'s name is {my_pet._Dog__name}')
else:
    print('my_pet has no name')
# my_pet's name is Rover

# hasattr() function is also used to check if a class has a class variable.
if hasattr(Dog, 'counter'):
    print(f'Dog\'s counter is {Dog.counter}')
else:
    print('Dog has no counter')
# Dog's counter is 3

print(my_pet.counter) #3
print(kates_pet.counter) #3
print(adams_pet.counter) #3
print(Dog.counter) # 3 Preferably use the class name to access the class variable.
# The counter variable is a class variable that is shared by all instances of the class.

# __dict__ only shows instance variables and ignores class variables.
# Look at the class definition itself to check the class variables.
print(my_pet.__dict__) # {'name': 'Rover', 'age': 5}


class Cat():
    __counter = 0
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Cat.__counter += 1

print(Cat._Cat__counter) # 0
# __dict can also shows the class variables.
print(Cat.__dict__) # {'__module__': '__main__', '_Cat__counter': 0, '__init__': <function Cat.__init__ at 0x7f6320805760>, '__dict__': <attribute '__dict__' of 'Cat' objects>, '__weakref__': <attribute '__weakref__' of 'Cat' objects>, '__doc__': None}

# __name__ is a special variable that is used to store the name of the module or class.
print(Cat.__name__) # Cat
print(type(my_pet)) # <class '__main__.Dog'>
print(type(my_pet).__name__) # 'Dog'
# type(my_pet).__name__ is used to get the name of the class of the object.
print(Dog.__module__) # '__main__'
