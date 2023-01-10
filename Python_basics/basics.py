#variable
x = 42
x: int = 42       #type hint to increase readability

#finding interest
principal = 1000
num_year = 3
rate = 0.05

year = 1
while year <= num_year:
    principal = principal * ( 1 + rate)
    print(year, principal)
    year +=1

print(f'{year:>3d}{principal:0.2f}')

#Arithmetic Operators
print(2 + 3)
print(10 - 5)
print(2 * 2.5)
print(25 / 5)
print(11 // 2)
print(2**2 + 1)
print(11 % 6)

#common mathematic function
print(abs(-5.3))
print(divmod(11, 6))
#round(3.3, [3]) not working

#shortened operation
y = 1
x = x + 1
y = y * 1

x += 1
y *= 1
#This can be used with the any operator

#conditional and control flow
a = 1
b = 2
if a < b:
    print('Computer says Yes')
else:
    print('Computer says No')

#to create an empty clause use pass
if a < b:
    pass        # Do nothing
else:
    print('Computer says No')

#to handle multiple cases , use the elif statement

maxval = a if a > b else b
if a > b:
    maxval = a
else:
    maxval = b

# walrus operator
x = 0
while (x := x + 1) < 10:
    print(x)

#break
x = 0
while x < 10:
    if x == 3:    # At innermost
        break
    print(x)
    x += 1
print('Done')

#continue
y = 0
while y < 10:
    y += 1
    if y == 3:
        continue  #skip printing 3
    print(y)
print('Done')

#text strings
a = "Hello World"
b = '''Hello World'''
c = 'Hello World'
d = """Hello World"""
print(a, b, c, d)


