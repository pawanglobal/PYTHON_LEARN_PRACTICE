motorcycles = ['yamaha', 'ducati', 'honda']
print(motorcycles)

motorcycles[0] = 'suzuki'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

cars = []
cars.append('suzuki')
cars.append('mahindra')
cars.append('tata')

print(cars)

cars.insert(0, 'tesla')
print(cars)

del cars[0]
print(cars)

popped_cars =  cars.pop()
print(cars)
print(popped_cars)