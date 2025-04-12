'''5-2. More Conditional Tests: You don’t have to limit the number of tests you cre-
ate to 10. If you want to try more comparisons, write more tests and add them

to conditional_tests.py. Have at least one True and one False result for each of
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list'''

name: str = "Cristiano"
username: str = "cristiano03"
age: int = 20
animals: list[str] = ["Dog", "Cat", "Shark", "Kangaroo", "Owl", "Fish", "Lizard", "Ant", "Penguin", "Duck", "Pidgeon", "Wolf", "Koala", "Lion", "Gazelle"]
candies: int = 4
money: float = 278.19
print("--------------------------------------------------------")

#String: equality True
print("Is his name Cristiano?")
print(name == "Cristiano")
print("--------------------------------------------------------")

#String: equality False
print("Is his name Christian?")
print(name == "Christian")
print("--------------------------------------------------------")

#String: inequality True
print("His name wasn't Giacomo, was it?")
print(name != "Giacomo")
print("--------------------------------------------------------")

#String: inequality False
print("His name wasn't Cristiano, was it?")
print(name != "Cristiano")
print("--------------------------------------------------------")

#String: .lower() True
print("He typed \"crIsTiaNo03\" in the login. Would it still work?")
print(username == "crIsTiaNo03".lower())
print("--------------------------------------------------------")

#String: .lower() False
print("He typed \"cHriStiaN03\" in the login. Would it still work?")
print(username == "cHriStiaN03".lower())

#Numerical: equality
print("Does he have 4 candies?")
print(candies == 4)
print("--------------------------------------------------------")

#Numerical: inequality
print("He didn't have exactly 4, right?")
print(candies != 4)
print("--------------------------------------------------------")

#Numerical: greater than or equal to
print("Can he buy that 19,99€ hamburger?")
print(money >= 19.99)
print("--------------------------------------------------------")

#Numerical: less than
print("I am pretty sure he does not have enough candies to give them all to all of their 28 classmates")
print(candies <= 28)
print("--------------------------------------------------------")

#Or True
print("Does he have 200€? or at the very least can he give me six candy?")
print(money >= 200 or candies >= 6)
print("--------------------------------------------------------")

#Or False
print("Does he have 2000€? or at the very least can he give me six candy?")
print(money >= 2000 or candies >= 6)
print("--------------------------------------------------------")

#And True
print("Is he a young adult?")
print(age >= 18 and age < 34)
print("--------------------------------------------------------")

#And False
print("Is he 18? if so can he buy me the most expensive beer?")
print(age >= 18 and money >= 1499.99)
print("--------------------------------------------------------")

#List: In it, True
print("Are dogs real animals?")
print("dog".title() in animals)
print("--------------------------------------------------------")

#List: In it, False
print("Are dragons real animals?")
print("dragon".title() in animals)
print("--------------------------------------------------------")

#List: not in it, True
print("Carrots aren't animals, right?")
print("carrot".title() not in animals)
print("--------------------------------------------------------")

#List: not in it, False
print("Wolves are not animals, right?")
print("wolf".title() not in animals)
print("--------------------------------------------------------")