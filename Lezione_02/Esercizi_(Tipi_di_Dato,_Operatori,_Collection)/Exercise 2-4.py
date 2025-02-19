'''Exercise 2-4
Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.'''

name: str = input("Type the person's name:\n>\t")
print(f'If "{name}" had to be in uppercase: {name.upper()}')
print(f'If "{name}" had to be in lowercase: {name.lower()}')
print(f'If "{name}" had to be written like a title: {name.title()}')