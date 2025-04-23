class Vehicle:
    class_message = "This is a message from vehicle class"
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle):
    def __init__(self, speed, wheels):
        Vehicle.__init__(self, speed)
        # super().__init__(speed)  # This is a more Pythonic way to call the constructor of superclass
        self.wheels = wheels
        print(Vehicle.class_message)  # Accessing class variable from superclass
        print(super().class_message)

    def speed_up(self):
        self.speed+=10
class WaterVehicle(Vehicle):
    pass

class Car(LandVehicle):
    def super_speed_up(self):
        super().speed_up()
        super().speed_up()
        super().speed_up()
        print(f"Car speed is now {self.speed}")

print(issubclass(Car, LandVehicle))  # True
print(issubclass(Car, Vehicle))  # True
print(issubclass(LandVehicle, Vehicle))  # True
print(issubclass(Car, Car))  # True

my_car = Car(100, 4)
print(my_car.__dict__) # {'speed': 100, 'wheels': 4}
my_car.super_speed_up()  # Car speed is now 130
print(my_car.__dict__) # {'speed': 130, 'wheels': 4}
my_car.speed_up()  # This will call the speed_up method from LandVehicle
print(my_car.__dict__) # {'speed': 140, 'wheels': 4}
print(my_car.class_message)  # This is a message from vehicle class