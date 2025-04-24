numbers = [i for i in range(1,101) if i % 3 != 0]

print('The numbers that are not divisible by 3 are:')
print(numbers)

binary_numbers = [0 if i%2 == 0 else 1 for i in range(100)]
print('The binary numbers are:')
print(binary_numbers)

nested_list = [[i for i in range(1,6)] for j in range(5)]
print('The nested list is:')
print(nested_list)