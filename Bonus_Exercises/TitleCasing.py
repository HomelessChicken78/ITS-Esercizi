'''Data una stringa in input, stampare stringa la prima lettera di ogni parola in maiuscolo'''

#Ask the string in input
string: str = input("Inserisci una stringa:\n>\t")

string = string.title()

'''#Split it in a list thanks to .split
splitted: list[str] = string.split()

for i in splitted:
    splitted[i] = splitted[i].title'''

print(f"\n---------------------------------------\n\nEcco la nuova stringa:\n\"{string}\"")