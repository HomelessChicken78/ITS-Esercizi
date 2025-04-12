'''6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city.
Print each piece of information stored in your dictionary.'''

from typing import Any

person: dict[Any] = {"first_name" : "Rachele", "last_name" : "Colonne", "age" : 22, "city" : "Brescia"}
for key, info in person.items():
    print(f"Il valore di {key} è: {info}")