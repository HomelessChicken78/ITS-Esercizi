'''
Scrivi una funzione che prenda una lista di numeri e ritorni un dizionario che
classifichi i numeri in liste separate per numeri positivi e negativi.

[0, 42, -2, 51, 103, -55] -> {"pari" : [0, 42, -2], "dispari" : [51, 103, -55]}
'''

def even_odd(ls: list[int|float]) -> dict[str, list[int|float]]:
    return {"even" : [n for n in ls if n%2 == 0], "odd" : [n for n in ls if n%2 != 0]}

if __name__ == "__main__":
    print(even_odd([0, 42, -2, 51, 103, -55]))