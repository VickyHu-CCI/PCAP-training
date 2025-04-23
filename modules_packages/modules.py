
import math
import sys
import random 
import platform

sys.path.append('../lib_path')  # Add the sibling directory to the system path
print(sys.path)

try:
    import surfshop  # Import the surfshop module after appending lib_path to sys.path
except ModuleNotFoundError:
    raise ModuleNotFoundError("Ensure '../lib_path' contains 'surfshop.py' or adjust the path.")

print(surfshop.__name__)  # surfshop
print(surfshop.__file__)  # Print the file path of the module

# PCAP exame:
# math.ceil() # Round up to the nearest integer
# math.floor() # Round down to the nearest integer
# math.trunc() # Truncate the decimal part
# math.factorial() # Calculate the factorial of a number 
# math.sqrt() # Calculate the square root
# math.hypot() # Calculate the hypotenuse of a right triangle
# random.seed(0) # Set the seed for reproducibility
# random.choice(['surfboard', 'wetsuit', 'sunglasses']) # 'surfboard'
# random.sample(['surfboard', 'wetsuit', 'sunglasses'], 2) # ['wetsuit', 'surfboard']
# random.random() # 0.0 <= x < 1.0
print(platform.platform(aliased=True, terse=True)) # return 'Windows-10-10.0.22621-SP0'
print(platform.machine()) # return machine type 'AMD64'
print(platform.processor()) # return processor name 'Intel64 Family 6 Model 158 Stepping 9, GenuineIntel'
print(platform.system()) # return system name 'Windows'
print(platform.python_implementation()) # return python implementation 'CPython'
print(platform.python_version_tuple()) # return python version tuple ('3', '11', '10')
print(platform.version()) # return system's release version #1 SMP Tue Nov 5 00:21:55 UTC 2024
print(sys.path) # return the list of directories that Python searches for modules



# for name in dir(sys):
#     if name.startswith('path'):
#         print(f'Name sart with path: {name}')
#     else:
#         print(f'name: {name}')

# Override the add_surfboards function
def custom_add_surfboards(quantity: int = 1) -> str:
    return f'Custom add_surfboards function called with quantity: {quantity}'

surfshop.add_surfboards = custom_add_surfboards

print(surfshop.add_surfboards(2))

print(surfshop.add_surfboards(10))

print(surfshop.add_surfboards())
