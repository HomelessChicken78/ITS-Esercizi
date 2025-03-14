'''Imagine you're participating in a Mario Kart race with your friends. Each player finishes
their race in a specific position.
Write a Python program that takes as input the finishing position of a player, given a positive integer,
and returns the position in cardinal form (e.g, "1st", "2nd", "3rd", "4th", "5th", etc.).'''

'''Solution I - If, Elif & Else
n: int = int(input("Write a position: "))
if (n == 1):
    print("1st")
elif (n == 2):
    print("2nd")
elif (n == 3):
    print("3rd")
else:
    print(f"{n}th")'''

'''Solution II - Match'''
n: int = int(input("Write a position: "))
match n:
    case 1:
        print("1st")
    case 2:
        print("2nd")
    case 3:
        print("3rd")
    case _:
        print(f"{n}th")