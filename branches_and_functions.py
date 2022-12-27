from sys import exit

def gold_room():
    print("This room is full of gold. How much Do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Oh!!! man, learn how to type a number.")
    if how_much < 50:
        print("You are not greedy, Congratulations!!! you can take the gold.")
        exit(0)
    else:
        dead("You are dead, you are a greedy person!!!.")

def dead(why):
    print(why, "Great job!!!")
    exit(0)


print(gold_room())