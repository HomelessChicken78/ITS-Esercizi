'''Scrivi una funzione che ruota gli elementi di una lista verso sinistra di un numero specificato k di posizioni.
La rotazione verso sinistra significa che ciascun elemento della lista viene spostato a sinistra di una posizione e
l'elemento iniziale viene spostato alla fine della lista.
Per la rotazione utilizzare lo slicing e gestire il caso in cui il numero specificato di posizioni sia maggiore della lunghezza della lista.

print(rotate_left([1, 2, 3, 4, 5], 2))
[3, 4, 5, 1, 2]
'''

def rotate_left(elements: list, k: int) -> list:
    if k > len(elements):
        k -= len(elements)
    new_list: list = []
    new_list = elements[k:]
    for i in elements[:k]:
        new_list.append(i)
    return new_list

if __name__ == "__main__":
    print(rotate_left([1, 2, 3, 4, 5], 8))