'''
Cristalli Condivisi
Davanti a due sfere gemelle devi estrarre solo ciò che riecheggia in entrambe.
Invoca `intersection_sorted(a, b)` per restituire la lista **ordinata** degli interi presenti sia in `a` sia in `b`, senza duplicati.
Mantieni la firma e apri il varco dei test.'''

def intersection_sorted(a: list[int], b: list[int]) -> list[int]:
    c: list[int] = []

    for el in a:
        if el in b and el not in c:
            c.append(el)
    
    return sorted(c)

if __name__ == "__main__":
    print(intersection_sorted([4, 3, 2, 5], [1, 2, 3]))

'''Le sfere cristalline mostrano solo le figure condivise: Cristalli Condivisi risolti.'''