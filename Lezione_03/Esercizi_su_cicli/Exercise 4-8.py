'''4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python.
Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.'''


for i in range(1, 11):
    print(f"The cube of {i} is {i ** 3}")

#WANT TO SAVE THE CUBES IN A LIST?
'''cubes: list[int] = []

#Fill in the list
for n in range(1, 11):
    cubes.append(n**3)

#Print the result
for res in cubes:
    print(f"The cube is {res}")'''