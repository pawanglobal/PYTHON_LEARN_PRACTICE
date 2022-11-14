my_foods = ['pizza', 'veg', 'salad', 'eggs']
friend_foods = my_foods[:]

my_foods.append('ice cream')
friend_foods.append('alcohal')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend favorite foods are:")
print(friend_foods)

print(f"\nThe first Three items of my foods are: {my_foods[0].upper()}, {my_foods[1].upper()},and {my_foods[2]}.upper().")

print("\nThe first Three items of my foods are:")
for favorite in my_foods[0:3]:
    print(favorite)
    
    
print("\nLast three item of my foods are:")
for favorite in my_foods[-3:]:
    print(favorite)