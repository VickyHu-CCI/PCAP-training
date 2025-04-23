'''
Python's MRO(Method Resolution Order) is the order in which Python looks for a method in a hierarchy of classes:
1. Look inside the object class
2. If not found, look in the superclass from left to right
3. If not found, show an error
'''

class Vehicle():
    def go(self):
        print("Going")
    def introduce(self):
        print("I am a vehicle")

class Flyable():
    def fly(self):
        print("Flying")

    def introduce(self):
        print("I am a flyable")

class Airplane(Vehicle, Flyable):
    # def introduce(self):
    #     print("I am an airplane") 
    # if Airplane class has its own introduce method, it will override the one from Vehicle and Flyable classes
    pass

my_airplane = Airplane()
my_airplane.go()  # Going
my_airplane.fly()  # Flying
my_airplane.introduce()  # I am a vehicle
