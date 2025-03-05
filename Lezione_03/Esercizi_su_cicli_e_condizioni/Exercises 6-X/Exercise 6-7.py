'''6-7. People: Start with the program you wrote for Exercise 6-1.
Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
Loop through your list of people. As you loop through the list, print everything you know about each person.
'''

from typing import Any

Rachele: dict[Any] = {"first_name" : "Rachele", "last_name" : "Colonne", "age" : 22, "city" : "Brescia"}
Lois: dict[Any] = {"first_name" : "Lois", "last_name" : "Chiocciola", "age" : 19, "city" : "Roma"}
Marta: dict[Any] = {"first_name" : "Marta", "last_name" : "Scriba", "age" : 20, "city" : "Fiumicino"}
people: list[dict] = [Rachele, Lois, Marta]

print("\n-----------------------\n")

for person in people:
    for key, value in person.items():
        print(f"{key} = {value}")
    print("\n-----------------------\n")