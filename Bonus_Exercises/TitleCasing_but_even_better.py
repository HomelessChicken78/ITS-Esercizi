'''Data una stringa in input, stampare stringa la prima e l'ultima lettera di ogni parola in maiuscolo'''


#Ask the string in input
string: str = input("Inserisci una stringa:\n>\t")
string = string.title()

#Split the string
many_words: list[str] = string.split()

result: list[str]  = []

for singular_word in many_words:
    almost_all: str = singular_word[:-1]
    last: str = singular_word[-1]
    full = almost_all + last.upper()
    result.append(full)

#Output
print(f"\n---------------------------------------\n\nEcco la nuova stringa:\n\"", end="")
print(" ".join(result), end="")
print("\"")