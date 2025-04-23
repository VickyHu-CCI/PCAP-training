class AnimalValueError(ValueError):
    """Custom exception for animal-related errors."""
    pass

def produce_animal_sound(animal_type:str):
    """Produce an animal sound based on the animal type."""
    if animal_type == 'dog':
        print ('Woof!')
    elif animal_type == 'cat':
        print('Meow!') 
    elif animal_type == 'cow':
        print('Moo!') 
    else:
        raise AnimalValueError(f"Unknown animal type: {animal_type}")

try:   
    produce_animal_sound('dog') # 'Woof!'
    produce_animal_sound('cat') # 'Meow!'
    produce_animal_sound('pig') # 'Unknown animal type: pig'
    produce_animal_sound('cow') # not executed
except AnimalValueError as e:
    print(e)

class UserActionException(Exception):
    """Custom exception for user action errors."""
    def __init__(self, message:str = '', user_id:str = ''):
        super().__init__()
        self.message = message
        self.user_id = user_id

    def __str__(self):
        return type(self).__name__ + 'occurred. Error message: ' + self.message + ', User ID: ' + self.user_id

class EmptyNameException(UserActionException):
    """Custom exception for empty name errors."""
    def __init__(self, user_id:str):
        super().__init__('An empty name was provided', user_id)
        self.user_id = user_id
    
def say_hello(name:str, user_id:str):
    """Say hello to the user."""
    if name == '':
        #raise UserActionException('Name cannot be empty', user_id)
        raise EmptyNameException(user_id)
    print(f'Hello {name}!')

try:
    say_hello('Adam', 'DT234')
    say_hello('', 'DT234')
    say_hello('John', 'DT234') # not executed
except Exception as e:
    print(e)