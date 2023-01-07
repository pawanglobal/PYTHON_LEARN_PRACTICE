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

