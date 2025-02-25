'''4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max()
to make sure your list actually starts at one and ends at one million.
Also, use the sum() function to see how quickly Python can add a million numbers.'''

to_one_million: list = []

#Fill the list
for i in range(1, 1000001):
    to_one_million.append(i)

print(f"Il numero più piccolo è {min(to_one_million)}\nMentre quello più grande è {max(to_one_million)}")