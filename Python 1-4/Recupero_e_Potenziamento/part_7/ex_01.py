def baricentro(v: list[int]) -> int|None:
    '''Determina se per tale lista esiste il baricentro,
    ovvero esiste un indice i per cui vale la formula scritta sopra.
    Se esiste ritornare l'indice, se non esiste ritornare None.'''
    count: int = 0
    for i in range(len(v)):
        count += 2
        if sum(v[:i+1]) == sum(v[i+1:]):
            return i, count

    return None, count

def printResult(v: list[int]) -> None:
    '''Stampi a schermo se esiste o meno il baricentro della lista v.
    Nel caso in affermativo, si mostri in output l'indice che definisce il baricentro.'''
    baricentro1 = baricentro(v)[0]

    if baricentro1:
        print(f"Esiste il baricentro del vettore v={v} ed è dato dall'indice i={baricentro1}")
    else:
        print(f"Il baricentro del vettore v={v} non esiste!")

def baricentroOttimizzato(v: list[int]) -> bool:
    tot: int = sum(v)
    current_sum: int = 0
    count: int = 0

    for i in range(len(v)):
        current_sum += v[i]
        count += 1
        if current_sum == tot - current_sum:
            return True, count
    return False, count

if __name__ == "__main__":
    # printResult([1, 2, 3, 3, 2, 1])
    # printResult([1, 3, 1, 2, -1])
    # print(baricentroOttimizzato([1, 2, 3, 3, 2, 1]))
    
    v1 = [1, 2, 3, 2, 5, 2, 1]
    v2 = [2, 0, -1, 4, 6, 3, -1]
    printResult(v1)
    printResult(v2)

    print(f"Dimostrazione che baricentro() fa più accessi di baricentroOttimizzato():\n{baricentro(v1)[1]} > {baricentroOttimizzato(v1)[1]}")
    print(f"Dimostrazione che baricentro() fa più accessi di baricentroOttimizzato():\n{baricentro(v2)[1]} > {baricentroOttimizzato(v2)[1]}")
