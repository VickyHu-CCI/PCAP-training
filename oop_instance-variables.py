class Dog():
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_pet = Dog('Rover', 5)
print(my_pet.__dict__) # {'name': 'Rover', 'age': 5}
my_pet.color = 'brown'
print(my_pet.__dict__) # {'name': 'Rover', 'age': 5, 'color': 'brown'}
del my_pet.age
print(my_pet.__dict__) # {'name': 'Rover', 'color': 'brown'}
# The __dict__ attribute of an object is a dictionary that contains all the attributes of the object.
# The __dict__ attribute is a built-in attribute of all Python objects
# and is used to store the attributes of the object.
# The __dict__ attribute is a mutable mapping object that can be modified at runtime.
# The __dict__ attribute is a dictionary that contains the object's attributes and their values.
# The __dict__ attribute is a read-only attribute that cannot be modified directly.

class Cat():
    def __init__(self, name, age):
        # Name mangling
        # is a technique used to make the name of an attribute or method in a class unique
        # by adding a prefix to the name.
        self.__name = name
        self.age = age
  
my_cat = Cat('Whiskers', 3)
print(my_cat.__dict__) # {'_Cat__name': 'Whiskers', 'age': 3}
# The __name attribute is a private attribute that cannot be accessed directly from outside the class.
# But you can access it using the _Cat__name to access the private attribute.
print(my_cat._Cat__name) # Whiskers
# Private attributes are only used inside the class and cannot be added from the outside the class.
my_cat.__breeth = 'Siamese'
print(my_cat.__dict__) # {'_Cat__name': 'Whiskers', 'age': 3, '__breeth': 'Siamese'}
