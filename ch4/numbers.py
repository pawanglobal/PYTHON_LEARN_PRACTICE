numbers = []
for value in range(1,21):
    number = value
    numbers.append(number)
    
print(numbers)
    
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1,21,2))
print(odd_numbers)

multiple_of_3 = list(range(3,31,3))
for numbers in multiple_of_3:
    print(numbers)
    
cubes = []
for value in range(1,10):
    cube = value**3
    cubes.append(cube)
print(cubes)

cubes = [value**3 for value in range(1,10)]
print(cubes)