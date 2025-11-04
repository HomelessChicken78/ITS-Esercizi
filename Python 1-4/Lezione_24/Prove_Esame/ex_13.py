'''Scrivi una funzione che prende una lista di numeri e ritorna un dizionario che classifica i numeri in liste separate per numeri pari e dispari.'''
def classifica_numeri(lista: int) -> dict[str:list[int]]:
    return {"pari" : [num for num in lista if num % 2 == 0], "dispari" : [num for num in lista if num % 2 != 0]}