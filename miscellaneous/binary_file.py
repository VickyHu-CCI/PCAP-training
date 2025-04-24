# 1 byte = 8 bits, which means 1 byte can represent 256 different values (0-255)

# Create a bytearray of size 100 bytes
# Default value for each byte is 0, in ASCII means Null
data = bytearray(100)
data[0] = 65  # ASCII value for 'A'
data[1] = 120  # ASCII value for 'x'
data[2] = 126  # Maximum value for a byte
data[3] = 100  # Maximum value for a byte

try:
    stream = open('file.bin', 'wb') # 'wb' means write binary
    stream.write(data)
    
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    stream.close()

# Read the binary file
try:
    stream = open('file.bin', 'rb')
    byte_array = stream.read(100)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    stream.close()
print(byte_array)
print(type(byte_array)) # <class 'bytes'>

#convert bytearray to hexadecimal
print('\n------------Hexadecimal representation:')
for byte in byte_array:
    print(hex(byte), end=' ')

# convert bytearray to integer
print('\n------------Integer representation:')
for byte in byte_array:
    print(int(byte), end=' ')

# read only 10 bytes from the bytearray
print('\n------------Reading only 10 bytes:')
try:
    bf = open('file.bin', 'rb')
    ba = bf.read(10)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    bf.close()

for byte in ba:
    print(int(byte), end=' ')

# Read as bytearray
print('\n------------Reading as bytearray:')
try:
    bf = open('file.bin', 'rb')
    # readinto() reads bytes from the file into the bytearray
    # The number of bytes read is returned
    # readinto() reads the file into the bytearray
    ba = bf.readinto(data)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    bf.close()

print(f"Bytes read: {ba}") # 100
print(data)
print(type(data)) # <class 'bytearray'>

  
