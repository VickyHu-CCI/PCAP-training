class Vehicle:
    class_message = "This is a message from vehicle class"
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle):
    def __init__(self, speed, wheels):
        Vehicle.__init__(self, speed)
        # super().__init__(speed)  # This is a more Pythonic way to call the constructor of superclass
        self.wheels = wheels
        print(super().class_message)

    def speed_up(self):
        self.speed+=10

class Car(LandVehicle):
    def super_speed_up(self):
        super().speed_up()
        super().speed_up()
        super().speed_up()
        print(f"Car speed is now {self.speed}")

my_vehicle = Vehicle(50)
my_land_vehicle = LandVehicle(60, 4)
my_car = Car(70, 4)

print(isinstance(my_vehicle, Vehicle))  # True
print(isinstance(my_land_vehicle, Vehicle))  # True
print(isinstance(my_car, Vehicle))  # True

print(isinstance(my_vehicle, LandVehicle))  # False
print(isinstance(my_land_vehicle, LandVehicle))  # True
print(isinstance(my_car, LandVehicle))  # True

print(isinstance(my_vehicle, Car))  # False
print(isinstance(my_land_vehicle, Car))  # False
print(isinstance(my_car, Car))  # True

# is always compares the objects the variables are pointing to
my_new_car = my_car
print('compare my_car and my_new_car:')
print(my_car is my_new_car)  # True
print('compare the dict of each:')
print(my_car.__dict__, my_new_car.__dict__)  # {'speed': 70, 'wheels': 4} {'speed': 70, 'wheels': 4}
my_car.speed_up()
print('The dict of each after speed up:')
print(my_car.__dict__, my_new_car.__dict__)  # {'speed': 80, 'wheels': 4} {'speed': 80, 'wheels': 4}

# It's different when initializing a new object of car
my_land_vehicle = LandVehicle(60, 4)
my_second_land_vehicle = LandVehicle(60, 4)
print(my_land_vehicle.__dict__, my_second_land_vehicle.__dict__) #{'speed': 60, 'wheels': 4} {'speed': 60, 'wheels': 4}
print('compare my_land_vehicle and my_second_land_vehicle:')
print(my_land_vehicle is my_second_land_vehicle)  # False
my_land_vehicle.speed_up()
print('The dict of each after speed up:')
print(my_land_vehicle.__dict__, my_second_land_vehicle.__dict__)  # {'speed': 70, 'wheels': 4} {'speed': 60, 'wheels': 4}

# String is immutable, so when munipulate a string, python creates a new string object
my_string = "hello"
my_new_string = 'hell'
my_new_string += 'o'
third_string = 'hello'
print(my_string is my_new_string)  # False
print(my_string == my_new_string)  # True
print(my_string is third_string)  # True

my_num = 5
the_num = 2
the_num += 3
print(my_num is the_num)  # True

# tuple is immutable, so when munipulate a tuple, python creates a new tuple object
# print((2,3) is (3,2)) # False
print('compare the value of two tupes:', end=' ')
print((2,3) == (3,2)) # False

# set is mutable, so when munipulate a set, python creates a new set object
# print({2,3} is {3,2}) # False
print('compare the value of two sets:', end=' ')
print({2,3} == {3,2}) # True
first_set = {1,2,3,4}
second_set = {1,2,3,4}
third_set = {1,2,3,4,5}
print(first_set is second_set)  # False
first_set.add(5)
print(first_set is third_set)  # False