'''Prossimo: Più avanti seguirai il battito dei multipli di tre e cinque fino al limite del tamburo.

Tamburo dei Multipli
Un tamburo bronzeo batte ritmi di tre e cinque; il varco risponde alla loro somma: evoca `sum_multiples(limit)`
per restituire la somma di tutti i numeri **minori di** `limit` divisibili per `3` **oppure** `5`.
Se `limit` ≤ `0`, torna `0`. Mantieni la firma e soddisfa i test.'''

def sum_multiples(limit: int) -> int:
    count: int = 0
    tot: int = 0

    if limit <= 0:
        return 0

    while count < limit:
        if count % 3 == 0 or count % 5 == 0:
            tot += count
        count += 1

    return tot

'''Hai separato le correnti pari e dispari come chiesto dagli spiriti del ponte.'''