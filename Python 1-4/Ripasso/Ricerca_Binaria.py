'''
Ricerca Binaria
Implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati
e ritorna True se il numero è all’interno del della lista, altrimenti False.
'''

def binary_search(numbers: list[int], search: int) -> bool:
    indice_minimo: int = 0
    indice_meta: int = 0
    indice_massimo: int = len(numbers)-1  # ultimo indice della lista. Se la lista è composta da 300 elementi allora l'indice dell'ultimo elemento è 299

    
    while indice_minimo <= indice_massimo:
        # Calcola l'indice al centro - in pratica la media tra 0 e la lunghezza della lista
        indice_meta = (indice_minimo + indice_massimo) // 2

        # Controlla se il numero da cercare è più piccolo o più grande del numero in mezzo alla lista. Lascia la parte che rimane
        if search < numbers[indice_meta]:
            indice_massimo = indice_meta - 1  # Diminuisci high fino alla metà: non è compresa nell'altra metà della lista quindi l'indice massimo diventa la metà

        elif search > numbers[indice_meta]:
            indice_minimo = indice_meta + 1  # Aumenta indice_minimo fino alla metà: non è compresa nella prima metà della lista, quindi l'indice minimo diventa la metà
        
        # Se il numero non è ne maggiore ne minore al numero in mezzo allora è uguale. Allora il numero è stato trovato
        else:
            return True
        
    # Se eventualmente l'indice minimo diviene più grande dell'indice massimo, allora non si è mai entrati nell'else e si può ritornare False (se non ci fosse un while continuerebbe all'infinito arrivato a questo punto)
    return False

if __name__ == "__main__":
    print(binary_search([1, 3, 5, 7, 9], 3))
    print(binary_search([10, 20, 30], 20))
    print(binary_search([42, 39], 2))
    print(binary_search([], 0))
    print(binary_search([i for i in range(1000)], 856))
    print(binary_search([i for i in range(100000000)], 82185))
