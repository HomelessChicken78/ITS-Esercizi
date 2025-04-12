'''
Esercizio 3C-00B. Scrivere un programma in Python che chieda all'utente di inserire il proprio nome
e il proprio genere (specificato con "m" per maschio o "f" per femmina) e utilizzi lo statement match
per fornire una risposta adeguata da inserire in un documento di identita'.

- Se il valore di gender è "m", stampare il nome e il genere come Maschio.
- Se il valore di gender è "f", stampare il nome e il genere come Femmina.
- Se il valore di gender è diverso da "m" o "f", stampare un messaggio di errore,
indicando che non è possibile generare un documento di identità.

Expected Output:

Inserire nome: Luca
Inserire gender. Digitare m per maschio e f per femmina: m
Nome: Luca
Gender: Maschio

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Inserire nome: Anna
Inserire gender. Digitare m per maschio e f per femmina: f
Nome: Anna
Gender: Femmina

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Inserire nome: Alex
Inserire gender. Digitare m per maschio e f per femmina: x
Mi dispiace Alex, non e' possibile procedere con la generazione di un documento di identità!
'''

name: str = input("Quale è il tuo nome?\n>\t")
g: str = input("Inserire il tuo genere (f = femmina, m = maschio):\n>\t").lower()

print("\n-----------------------------------------------------\n")
match g:
    case "m":
        print(f"Nome: {name}\nGender: Maschio")
    case "f":
        print(f"Nome: {name}\nGender: Femmina")
    case _:
        print(f"Mi dispiace {name}, non e' possibile procedere con la generazione di un documento di identità!")