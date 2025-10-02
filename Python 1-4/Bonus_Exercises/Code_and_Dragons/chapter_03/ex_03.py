'''Prossimo: Preparati a svelare la differenza simmetrica che divide le due congreghe.

Scintille Divergenti
Le due sfere ora chiedono ciò che le separa: elementi che vibrano in **una sola** delle due.
Evocalo con `symdiff_sorted(a, b)`, restituendo la lista **ordinata** degli interi che compaiono esattamente in una delle liste.
Mantieni la firma e placa i test.'''

def symdiff_sorted(a: list[int], b: list[int]) -> list[int]:
    c: list[int] = []

    for el in a:
        if el not in b and el not in c:
            c.append(el)
    
    for el in b:
        if el not in a and el not in c:
            c.append(el)
    
    return sorted(c)

'''Hai distinto le scintille che non coincidono tra le sfere: Scintille Divergenti chiarite.'''