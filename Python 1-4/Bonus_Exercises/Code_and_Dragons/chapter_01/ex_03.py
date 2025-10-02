'''Prossimo: Più avanti dovrai zittire gli echi tenendo solo la prima traccia di ogni numero.

Eco delle Tracce
La terza navata risuona di echi ripetuti: per calmare il rimbombo, lascia parlare solo la prima voce di ogni numero.
Fallo con `dedup_stable(nums)`, che crea una nuova lista con la prima occorrenza di ciascun valore mantenendo l'ordine.
Mantieni la firma e placa i test.'''

def dedup_stable(nums: list[int]) -> list[int]:
    if not nums:
        return []
    
    new_list: list[int] = [nums[0]]

    for n in nums:
        if new_list[-1] != n:
            new_list.append(n)

    return new_list

'''Gli echi numerici sono quieti: Eco delle Tracce ora tace nella Biblioteca.'''