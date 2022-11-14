pizza = {
    'crust':'thick',
    'toppings':['mushrooms', 'extra cheese'],
    }
print(f"You have ordered the {pizza['crust']}-crust pizza"
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping.upper())