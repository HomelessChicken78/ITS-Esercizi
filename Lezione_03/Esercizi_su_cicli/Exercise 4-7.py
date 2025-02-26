'''4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.'''

threes: list[int] = []

#Fill in the list
for i in range(3, 31, 3):
    threes.append(i)

#Print the result
print("Multiple of 3 'till 30 are:")
for i in threes:
    print(i)