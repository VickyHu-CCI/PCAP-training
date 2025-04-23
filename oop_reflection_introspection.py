# Introspection is the ability of a program to check the type or properties of an object at runtime.
# Reflection is the ability of a program to change the properties or methods of an object at runtime.

def empty_string(user_object):
    for property_name in user_object.__dict__.keys():
        property_value = getattr(user_object, property_name)
        print(f'Property: {property_name}, Value: {property_value}')
        if isinstance(property_value, str):
            setattr(user_object, property_name, '')
    print(f'Object after empty_string: {user_object.__dict__}')
        

class Dog():
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def present(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')


my_dog = Dog('Rover', 5)
my_dog.present()
empty_string(my_dog)
my_dog.present()