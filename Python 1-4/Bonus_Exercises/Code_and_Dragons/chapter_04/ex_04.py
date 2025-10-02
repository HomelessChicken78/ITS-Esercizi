'''Prossimo: Tra un respiro dovrai imprigionare una costante dentro un gesto pronto ad aggiungere sempre la stessa forza.

Vincolo della Costante
Per aprire la Camera del Vincolo imprigiona una costante in un gesto che allunghi ogni mano che lo invoca: usa `curry_add(n)`
per restituire una funzione che sommi `n` al valore ricevuto. Mantieni la firma e soddisfa i test.'''

def curry_add(n):
    def h(m):
        return n + m
    return h

'''Hai imprigionato una costante nel gesto: il Vincolo della Costante risponde.'''