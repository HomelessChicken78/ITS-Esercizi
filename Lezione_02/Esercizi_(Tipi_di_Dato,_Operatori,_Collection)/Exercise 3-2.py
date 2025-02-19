'''Exercise 3-2
Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name,
print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.'''

names: list = ["Valeryia", "Rachele", "Francesca", "Giorgia", "Pingproxy"]

'''WITH FOR
for i in names:
    print(f"Hi {i}! How are you doing today?")'''

'''WITHOUT FOR'''
print(f"Hi {names[0]}! How are you doing today?")
print(f"Hi {names[1]}! How are you doing today?")
print(f"Hi {names[2]}! How are you doing today?")
print(f"Hi {names[3]}! How are you doing today?")
print(f"Hi {names[4]}! How are you doing today?")