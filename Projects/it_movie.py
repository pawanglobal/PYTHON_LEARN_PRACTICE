print ("""Bill and Ben are trapped in the Joker's house, and now they want
to move out from the house. There are two doors in the dark which 
door they should choose. Door 1 or Door 2.""")

door = input("> ")

if door == "1":
    print("Here is a giant snake eating a man.")
    print("what do you do?")
    print("1. Kill the snake!!!")
    print("2. Scream at snake.")

    snake = input("> ")

    if snake == "1":
        print("Snake eats your face off.")
    elif snake == "2":
        print ("Snake eats your legs off.")
    else:
        print(f"Well {snake} probably better.")
        print("Snake runs away.")
elif door == "2":
    print("You see a dark endless dark tunnel")
    print("dark tunnel says:")
    print("1. Die")
    print("2. Come to me")
    print("3. free")

    insanitny = input("> ")

    if insanitny == "2" or insanitny == "3":
        print("Well done! you are free to go.")
    elif insanitny == "1":
        print("You are not afraid of Death so you are free.")
    else:
        print("You are dead.")
else:
    print("You stumble around and fall on a knife and die.")
