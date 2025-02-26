'''Data una stringa in input, stampare stringa la prima e l'ultima lettera di ogni parola in maiuscolo'''


#Ask the string in input
string: str = input("Inserisci una stringa:\n>\t")
string = string.title()

#Split the string
word: list[str] = string.split()

result: list[str]  = []

for letter in word:
    almost_all: str = letter[:-1]
    last: str = letter[-1]
    full = almost_all + last.upper()
    result.append(full)

#Output
print(f"\n---------------------------------------\n\nEcco la nuova stringa:\n\"", end="")
print(" ".join(result), end="")
print("\"")