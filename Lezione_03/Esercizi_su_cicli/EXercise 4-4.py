'''4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers.
(If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)'''

to_one_million: list = []

#Fill the list
for i in range(1, 1000001):
    to_one_million.append(str(i))

print(", ".join(to_one_million))