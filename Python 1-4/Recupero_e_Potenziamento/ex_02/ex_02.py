'''
Esercizio 2. 
 
Elaborare uno schema che consenta di stampare in output in maniera ricorsiva gli elementi di una lista in ordine inverso.

Una volta elaborato il diagramma, appena consentitovi dal docente, scrivere una funzione ricorsiva in Python, chiamata printListBackward che stampi in output gli elementi di una lista in ordine inverso, sfruttando la ricorsione.
Infine, scrivere un codice driver date le seguneti liste, stampi ogni lista in ordine inverso sfruttando la funzione ricorsiva printListBackward.

    lista1: 1, 2, 3, 4, 5

    lista2: "Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"

'''

def print_reverse(words: list[str]) -> None:
    if not words:
        return
    else:
        last_index = len(words)-1
        print(words[last_index])
        print_reverse(words[:last_index])

print_reverse(["Armatura", "Bravura", "Cane", "Diamante", "Elefante", "Furfante"])