'''
 The __bases__ property of a class returns a tuple with all the base classes that the given class inherits from
'''

class Vehicle():
   pass
        
class Rideable():
   pass
      
class PetrolVehicle(Vehicle):
   pass
        
class Car(PetrolVehicle, Rideable):
   pass

# bases for Vehicle and Rideable
print(Vehicle.__bases__) # (<class 'object'>,)
print(Rideable.__bases__) # (<class 'object'>,)

# bases for PetorlVehicle
print(PetrolVehicle.__bases__) # (<class '__main__.Vehicle'>,)

# bases for Car
print(Car.__bases__) #(<class '__main__.PetrolVehicle'>, <class '__main__.Rideable'>)