'''Prossimo: Varcata la camera incontrerai le prove delle condizioni, governate dal giudizio.

Sala dell'Equilibrio
Nella Sala dell’Equilibrio ogni cifra viene giudicata: oscura, neutra o luminosa.
Tieni il verdetto con `sign(n)`: restituisci `-1` se `n` è negativo, `0` se è zero, `1` se è positivo.
Mantieni la firma esatta e lascia che i test ti aprano il passaggio.'''

def sign(n: int) -> int:
    if n == 0:
        return 0
    
    return -1 if n < 0 else 1

'''La Sala dell'Equilibrio riconosce il destino di ogni numero pronunciato.'''