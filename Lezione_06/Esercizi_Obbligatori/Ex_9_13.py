'''9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called
roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.'''

from random import randint

class Die:
    def __init__(self, sides: int = 6):
        self.sides = sides
    
    def roll_die(self) -> None:
        print(randint(1, self.sides))

print("Six sided dice:")
d6: Die = Die()
for roll in range(0, 10):
    d6.roll_die()

print("\nTen sided dice:")
d10: Die = Die(10)
for roll in range(0, 10):
    d10.roll_die()

print("\nTwenty sided dice:")
d20: Die = Die(20)
for roll in range(0, 10):
    d20.roll_die()