'''r5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd.
Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.'''

#Create a new list and fill it with numbers from 1 to 9
ordinal_numbers: list[int] = []
for i in range(1, 10):
    ordinal_numbers.append(i)

#Display each ordinal number:
for n in ordinal_numbers:
    if n == 1:
        print(f"{n}st")
    elif n == 2:
        print(f"{n}nd")
    elif n == 3:
        print(f"{n}rd")
    else:
        print(f"{n}th")
