'''4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list.
• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.'''

#Previous exercise
cubes: list[int] = []

#Fill in the list
for n in range(1, 11):
    cubes.append(str(n**3))

#Add several lines to the end of the program
print(f"The first three items are: ", end="")
print(", ".join(cubes[:3]))