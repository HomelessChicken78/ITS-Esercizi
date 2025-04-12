'''Scrivi una funzione che riceva in input due liste di interi della stessa lunghezza.
La funzione deve calcolare la somma elemento per elemento e restituire una nuova lista contenente i risultati.

For example:
print(somma_elementi([1,1,1],[1,1,1]))
>>>[2, 2, 2]'''

def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    z: list[int] = []
    i: int = 0
    if not (len(x) == len(y)):
        raise ValueError("The two lists must be of the same lenght")

    while i < len(x):
        z.append(x[i]+y[i])
        i += 1
    return z
    
if __name__ == "__main__":
    print(somma_elementi([0, 1, 2], [2, 1, 0]))