class Animal():
    def __init__(self):
        self.species = 'General Animal'

    def sound(self):
        print('Generic animal sound')

    def present(self):
        print(f'I am a {self.species} and I make this sound: ', end='')
        self.sound()



class Dog(Animal):
    def __init__(self):
        self.species = 'Dog'

    def sound(self):
        print('Woof! Woof!')

first_pet = Animal()
second_pet = Dog()
first_pet.present()  # I can do the following sound: Generic animal sound
print('--------------------------------')
second_pet.present()  # I can do the following sound: Woof! Woof!
