class Vehicle():
    def show_power_type(self):
        print("I can use power from various sources")

class ElectricVehicle(Vehicle):
    def show_power_type(self):
        print("I can use power from electricity")

class PetrolVehicle(Vehicle):
    def show_power_type(self):
        print("I can use power from petrol")

class HybridCar(ElectricVehicle, PetrolVehicle):
    pass

# The MRO for HybridCar is: (HybridCar, ElectricVehicle, PetrolVehicle, Vehicle)
my_toyota_yaris = HybridCar()
my_toyota_yaris.show_power_type()  # I can use power from electricity