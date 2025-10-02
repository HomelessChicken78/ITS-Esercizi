'''Prossimo: Mentre la sala successiva si apre, la prossima sfida ti chiedera di contare quante torce emergeranno con luce pari.

Torce Pari
Nel corridoio delle torce, solo quelle pari restano accese insieme: conta quante sono invocando `count_even(nums)`,
che restituisce quante voci della lista sono **pari** (incluso `0`). Mantieni la firma e placa i test.'''

def count_even(nums: list[int]) -> int:
    even: int = 0

    for n in nums:
        if n % 2 == 0:
            even += 1
        
    return even

'''Hai previsto quante torce emetteranno luce pari nel teatro arcano.'''