'''r
Esercizio 3C-10. Scrivere un programma in Python che permetta all'utente di inserire una data
(giorno e mese espressi in forma numerica),
salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

- Capodanno → 1 Gennaio → "Capodanno"
- San Valentino → 14 Febbraio → "San Valentino"
- Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
- Ferragosto → 15 Agosto → "Ferragosto"
- Halloween → 31 Ottobre → "Halloween"
- Natale → 25 Dicembre → "Natale"
- Altro caso → "Nessuna festività importante in questa data."

Expected Output:

Inserisci il giorno: 25
Inserisci il mese: 12
Output: Il 25/12 è Natale!

- - - - - - - - - - - - - - -

Inserisci il giorno: 5
Inserisci il mese: 3
Output: Nessuna festività importante in questa data.
'''
#This serves as a guideline to know every month how many days has
date_rules: dict[int, int] = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
    }

#Insert in input the day and the month
day: int = int(input("Inserisci il giorno:\n>\t"))
month: int = int(input("Inserisci il mese:\n>\t"))

#Check if the month exists
while month not in range (1, 13):
    month: int = int(input("Mese non esistente. Inserisci il mese:\n>\t"))

#Checks if the day of that month exists
while day not in range (1, (date_rules[month])+1):
    day: int = int(input(f"Il giorno {day}/{month} non esiste. Inserisci il giorno:\n>\t"))

#Once you know the date exists, put it in a tuple
date: tuple[int, int] = (day, month)

#Do the match case to check if it is a festivity
match date:
    case (1, 1):
        print("Il giorno 01/01 è Capodanno!")
    case (14, 2):
        print("Il giorno 14/02 è San Valentino")
    case (*_, 6):
        print(f"Il giorno {date[0]}/{date[1]} è la Festa della Repubblica Italiana")
    case (15, 8):
        print("Il giorno 15/08 è Ferragosto")
    case (31, 10):
        print("Il giorno 31/10 è Halloween")
    case (25, 12):
        print("Il giorno 25/12 è Natale")
    case _:
        print("Nessuna festività importante in questa data.")