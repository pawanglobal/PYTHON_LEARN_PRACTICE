the_count = [1, 2, 3, 4]
fruits = ['Banana', 'Orange', 'Mango', 'grapes']
change = [1, 'penny', 2, 'rupees', 3, 'pounds']

for count in the_count:
    print(f"This is number {count}")

for fruit in fruits:
    print(f"I have one {fruit}.")

for i in change:
    print(f"I got {i}.")

elements = []

for i in range(0,6):
    print(f"I am adding {i} to the elements.")
    elements.append(i)

for i in elements:
    print(f"The elemen was:{i}")
