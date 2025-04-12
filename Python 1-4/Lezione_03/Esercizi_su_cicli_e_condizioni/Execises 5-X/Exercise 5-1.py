'''5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.'''
#o
color: str = "Blue"
money: float = 219.93
amount_candies: int = 5
light_on: bool = False

print("--------------------------------------------------------")
#Number 1: Is my light off?
print("Did i turn off the light? I predict True")
print(light_on == False)  #Is light_on == False? -> is False == False? -> Yes -> print(True) -> True
print("--------------------------------------------------------")

#Number 2: Am i rich?
print("Am i rich? Do i have 200.000€ or more? I predict False")
print(money >= 200000)  #Is money >= 200.000,00? -> is 219,93 >= 200.000? -> No -> print(False) -> False
print("--------------------------------------------------------")

#Number 3: Can i buy an overpriced hamburger?
print("Can i buy this 35€ hamburger? I predict True")
print(money >= 35)  #Is money >= 35,00? -> is 219,93 >= 35,00? -> Yes -> print(True) -> True
print("--------------------------------------------------------")

#Number 4: Can David receive a candy?
print("Can i give a candy to David? I predict True")
print(amount_candies >= 1)  #Is amount_candies >= 1? -> is 10 >= 1? -> Yes -> print(True) -> True
print("--------------------------------------------------------")

#Number 5: Is my favourite color Black?
print("Is my favourite color Black? I predict False")
print(color == "Black")  #Is color == "Black"? -> is "Blue" == "Black"? -> No -> print(False) -> False
print("--------------------------------------------------------")

#Number 6: Does my blue car have the light on?
print("Did i left the lights of my Blue car turned on? I predict False")
print(color == "Blue" and light_on == True)  #Is: Color == "Blue"? and: light_on == True? -> is "Blue" == "Blue"? and False == True? -> Yes and No -> print(True and False) -> print(False) -> False
print("--------------------------------------------------------")

#Number 7: Do i already have a blue shirt? if not can i buy it?
print("Do i have a blue shirt in my wardrobe? If not can i buy it? I predict True")
print(color == "Blue" or money >= 20)  #Is: Color == "Blue"? and: money >= True? -> is "Blue" == "Blue"? and 219,39 >= 20,00? -> Yes and Yes -> print(True or True) -> print(True) -> True
print("--------------------------------------------------------")

#Number 8: Candies and wealth
print("Am i rich? If not can i eat 5 candies? I predict True")
print(money >= 200000 or amount_candies >= 5)
print("--------------------------------------------------------")

#Number 9: Fix broken false
print("Is my light still on because it's broken? If yes, can i turn adjust it? I predict False")
print(light_on or money >= 230)
print("--------------------------------------------------------")

#Number 10:
print("I predict False")
print(light_on or (color == "Black" and money >= 2000))
print("--------------------------------------------------------")