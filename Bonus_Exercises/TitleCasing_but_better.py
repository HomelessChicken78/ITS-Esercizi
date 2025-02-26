'''Data una stringa in input, stampare stringa l'ultima lettera di ogni parola in maiuscolo'''


#Ask the string in input
string: str = input("Inserisci una stringa:\n>\t")[::-1]
string = string.title()

#Invert the string again
string = string[::-1]

#Output
print(f"\n---------------------------------------\n\nEcco la nuova stringa:\n\"{string}\"")