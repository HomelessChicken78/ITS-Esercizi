'''Exercise 3-3
Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car,
and make a list that stores several examples. Use your list to print a series of statements
about these items, such as “I would like to own a Honda motorcycle.'''

vehicles: list = ["Bugatti Centodieci", "Boing 747", "Tesla Model S", "Lamborghini Huracàn", "Submarine"]

'''WITH FOR
for i in vehicles:
    print(f"I would like to own a {i},")'''

'''WITHOUT FOR'''
print(f"I would like to own a {vehicles[0]}")
print(f"I want to buy a {vehicles[1]}")
print(f"I'd like to have a {vehicles[2]}")
print(f"Why i still didn't buy a {vehicles[3]} yet?")
print(f"Man, it would be cool to own a {vehicles[4]}!")
