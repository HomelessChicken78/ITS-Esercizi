'''
Si vuole calcolare la somma di tutti i prodotti x * y per tutti i valori interi di x (i cui valori variano tra 0 e 100)
e tutti i valori interi di y (i cui valori sono dati dalla sequenza 2, 4, 6, 8, 10, 12, ..., 88), ovvero i prodotti
1 * 2,
1 * 4,
...
1 * 88,
2 * 2,
2 * 4,
...
2 * 88,
...
100 * 2,
100 * 4,
...
100 * 88

Scrivere una funzione Python proDict() che senza ricevere alcun argomento in input, che restituisce un dizionario che abbia
come chiavi la tupla (x,y) e come valore x*y , in cui memorizzare tutti i prodotti x * y per tutti i valori interi di x e
tutti i valori interi di y.

Nel main, scrivere un codice Python che inizializzi un dizionario d ricorrendo alla funzione prodDict e stampare in output i
valori del dizionario d, per i seguenti valori di x e y:

    x = 13, y = 88

    x = 83, y = 56

    x = 71, y = 44
'''

def prodDict() -> dict[tuple[int, int], int]:
    res: dict[tuple[int, int], int] = {}
    
    for n1 in range(0, 101):
        for n2 in [n*2 for n in range(1, 45)]:
            res[(n1, n2)] = n1*n2

    return res

d = prodDict()
print(d[(13, 88)])
print(d[(83, 56)])
print(d[(71, 44)])