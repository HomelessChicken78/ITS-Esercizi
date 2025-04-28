'''
Scrivi una funzione che riceve una lista di numeri, filtra i numeri pari, e restituisce una nuova lista con i numeri pari moltiplicati per un fattore dato.

For example:
print(filtra_moltiplica([1, 2, 3, 4, 5, 6], 3))
>>>[6, 12, 18]

print(filtra_moltiplica([], 3))
[]'''

def filtra_moltiplica(lista_numeri: list[int], fattore: int) -> list[int]:
    return [x*fattore for x in lista_numeri if x % 2 == 0]

if __name__ == "__main__":
    print(filtra_moltiplica([1, 2, 3, 4, 5, 6], 3))  #[6, 12, 18]
    print(filtra_moltiplica([], 3))  #[]