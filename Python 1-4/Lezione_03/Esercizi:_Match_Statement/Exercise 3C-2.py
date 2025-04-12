'''r
Esercizio 3C-2. Scrivere un programma in Python che converta un voto di laurea italiano (sistema in 110-emi) nel sistema GPA americano (scala 0-4).
Il programma deve accettare in input un voto di laurea compreso tra 66 e 110, espresso come numero intero e usare un match per determinare il
corrispondente GPA americano, secondo questa tabella di conversione:

- 106-110 → 4.0
- 101-105 → 3.7
- 96-100 → 3.3
- 91-95 → 3.0
- 86-90 → 2.7
- 81-85 → 2.3
- 76-80 → 2.0
- 70-75 → 1.7
- 66-69 → 1.0overlap
- Altro caso → "Voto non valido"

Expected Output:

Inserisci il voto di laurea: 110
Output: GPA 4.0

- - - - - - - - - - - - - - - - -

Inserisci il voto di laurea: 65
Output: Voto non valido
'''

voto: str = input("Inserire un voto universitario tra 66 e 110:\n>\t")

if not voto.isnumeric():
    print("Perfavore inserire un numero!")
else:
    voto = int(voto)
    match voto:
        case voto if voto >= 106 and voto <= 110:
            print("GPA: 4.0")
        case voto if voto >= 101 and voto <= 105:
            print("GPA: 3.7")
        case voto if voto >= 96 and voto <= 100:
            print("GPA: 3.3")
        case voto if voto >= 91 and voto <= 95:
            print("GPA 3.0")
        case voto if voto >= 86 and voto <= 90:
            print("GPA 2.7")
        case voto if voto >= 81 and voto <= 85:
            print("GPA 2.3")
        case voto if voto >= 76 and voto <= 80:
          print("GPA 2.0")
        case voto if voto >= 70 and voto <= 75:
            print("GPA 1.7")
        case voto if voto >= 66 and voto <= 69:
            print("GPA 1.0")
        case _:
           print("Voto non valido")