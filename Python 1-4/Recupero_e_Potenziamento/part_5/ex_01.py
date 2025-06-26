from random import randint

def genera(dim: int) -> list[list[int]]:
    if dim <= 0:
        raise RuntimeError(f"Non è possibile creare una matrice con dimensioni pari ad {dim}")
    
    matrix: list[list[int]] = []

    for _ in range(dim):
        row: list[int] = []

        for j in range(0, dim):
            if j != 0:
                while True:
                    randomic = randint(0, 13)
                    if randomic != row[0]:
                        row.append(randomic)
                        break
            else:
                row.append(randint(0, 13))

        matrix.append(row)
        
    return matrix

def printMAT(mat: list[list[int]]) -> None:
    for row in mat:
        for cell in row:
            print(f"{cell:<5}", end="")
        print()

def somma(nums: list[int]) -> int:
    res = 0
    for n in nums:
        res += n
    return res

def calcolaCarico(mat: list[list[int]], row: int, col: int) -> int:
    '''Data una matrice quadrata di dimensione m x m, il carico di una posizione (r,c), indicato con k(r,c),
    è dato dalla differenza tra la somma degli elementi della riga r e la somma degli elementi della
    colonna c.'''
    column: list[int] = []
    for j in range(len(mat)):
        column.append(mat[j][col])
    return somma(mat[row]) - somma(column)

def caricoNullo(mat: list[list[int]]) -> list[tuple[int, int]]:
    '''Data in input una matrice, restituisce una lista di
    tuple, dove ogni tupla rappresenta una coppia di indici (r,c) per cui il carico della matrice è
    nullo. Ovvero, dovete trovare tutte le righe r e le colonne c per cui il carico della matrice
    k(r,c)=0 e memorizzare ogni coppia (tupla) in una lista.'''
    res: list[tuple[int, int]] = []

    for row in range(len(mat)):
        for cell in range(len(mat[row])):
            if calcolaCarico(mat, row, cell) == 0:
                res.append((row, cell))
            
    return res

def caricoMax(mat: list[list[int]]) -> list[tuple[int, int]]:
    '''Data in input una matrice restituisce una tupla di indici
    r e c per i quali si ha il carico massimo della matrice. Ovvero, dovete trovare la coppia di indice 
    riga r e indice colonna c per cui il carico k(r,c) ha valore massimo. Prima di restituire la tupla di
    indici (r,c) stampare il valore del carico massimo.'''
    max: int = 0

    for row in range(len(mat)):
        for cell in range(len(mat[row])):
            calcolato: int = calcolaCarico(mat, row, cell)
            if calcolato > max:
                max = calcolato
                res = (row ,cell)
            
    return res

def caricoMin(mat: list[list[int]]) -> list[tuple[int, int]]:
    '''Data in input una matrice restituisce una tupla di indici
    r e c per i quali si ha il carico minimo della matrice. Ovvero, dovete trovare la coppia di indice riga
    r e indice colonna c per cui il carico k(r,c) ha valore minimo. Prima di restituire la tupla di indici
    (r,c) stampare il valore del carico minimo.'''
    min: int = 99999999

    for row in range(len(mat)):
        for cell in range(len(mat[row])):
            calcolato: int = calcolaCarico(mat, row, cell)
            if calcolato < min:
                min = calcolato
                res = (row ,cell)
            
    return res



m1 = genera(5)
printMAT(m1)
print(calcolaCarico(m1, 0, 1))
print(caricoNullo(m1))
print(caricoMax(m1))
print(caricoMin(m1))