'''Functions/3: Exercise
Let’s try to define a function named subtract ourselves:
● It should take 2 parameters.
● Inside the function, it should subtract the two.
● Then, return the result.
After you defined it, call the function with some arguments'''

def subtract(first: int, second: int):
    result = first - second
    return result

print(subtract(57, 2))
print(subtract(3, 2))
print(subtract(4, 8))
print(subtract(-8, 3))
print(subtract(3, -2))