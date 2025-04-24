
# Read a file in Python
try:
    stream = open("sample_text.txt")
    print(stream.read(3))
    print(stream.read(6))
    print(stream.read())
    print(stream.read(3))  # This will return an empty string
    stream.close()  
except Exception as e:
    print(f"An error occurred: {e}")


# Read a file character by character
try:
    stream = open("sample_text.txt")
    character = stream.read(1)
    counter = 0
    while character != '':
        counter += 1
        print(character, end='-')
        character = stream.read(1)
    print(f"\nTotal characters read: {counter}")
    stream.close()
except Exception as e:
    print(f"An error occurred: {e}")

# Read a file line by line
try:
    stream = open("sample_text.txt")
    counter = 0
    line = stream.readline()
    while line != '':
        counter += 1
        print(line, end='-')
        line = stream.readline()
    stream.close()
    print(f"\nTotal lines read: {counter}")
except Exception as e:
    print(f"An error occurred: {e}")


# Read a file using readlines()
try:
    stream = open("sample_text.txt")
    lines = stream.readlines()
    print('Content of the lines var:', lines)
    print('Number of lines in the file:', len(lines))
    for line in lines:
        print(line, end='')
    stream.close()
except Exception as e:
    print(f"An error occurred: {e}")

# Reading more than one line at a time means better performance
# Read a file using readlines() reading all the lines at once may crush the memory
# Read a file using readlines() reading 3 lines at a time
try:
    stream = open("sample_text.txt")
    lines = stream.readlines(3)
    while len(lines) != 0:
        print(lines)
        for line in lines:
            print('-------------------------------------')
            print(line, sep='')
        lines = stream.readlines(3)
    stream.close()
except Exception as e:
    print(f"An error occurred: {e}")

# read the file by stream 
try:
    stream = open('sample_text.txt')
    for line in stream:
        print(line, end='') 
    # no need to close the stream, it will be closed automatically
except Exception as e:
    print(f"An error occurred: {e}")


# Write in the file
# 'w' mode will create a new file if it does not exist, or overwrite the existing file
try:
    stream = open('new_file.txt', 'w')
    stream.write('Hello World\n')
    stream.write('This is a new file\n')
    stream.write('This is the third line\n')
    stream.close()
except Exception as e:
    print(f"An error occurred: {e}")

