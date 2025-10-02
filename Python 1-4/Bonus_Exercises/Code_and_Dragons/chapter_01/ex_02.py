'''Prossimo: Mentre ti rimetti in cammino, il prossimo varco ti chiede di isolare il picco di energia nascosto tra le liste.

Picco della Lista
Con il foyer illuminato, le colonne di vetro rivelano onde di potere: il varco si apre solo al picco giusto.
Isolalo con `max_or_none(nums)`, restituendo il massimo in `nums` o `None` se è vuota.
Mantieni la firma e soddisfa i test come richiesto dal rituale.'''

def max_or_none(nums: list[int]) -> int | None:
    if not nums:
        return None

    maximum: int = float('-inf')

    for n in nums:
        if n > maximum:
            maximum = n
    
    return maximum

'''Nel foyer cristallino hai isolato il Picco della Lista che alimenta i portali.'''