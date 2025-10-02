'''
Benvenuto, assert False (Mago)

Ultimo custode della Biblioteca degli Specchi, raduni frammenti dispersi per ridare voce ai portali.
Dal Bastone degli Itinerari Arcani alla Tavola Armonica, ogni capitolo ti chiede logica e incanti
per risvegliare l'accademia dormiente.

Flusso dei frammenti
Le porte della Biblioteca degli Specchi si spalancano: frammenti numerici orbitano instabili.
Riuniscili in un unico flusso per riaccendere il foyer — concentra i frammenti pronunciando `sum_list(nums)`:
deve restituire la somma degli interi in `nums`; se `nums` è vuota, ritorna `0`.
Mantieni esattamente questa firma e fai in modo che i test si aprano come serrature.'''

def sum_list(nums: list[int]) -> int:
    tot: int = 0

    for n in nums:
        tot += n

    return tot

'''Gli specchi hanno ripreso a riflettere: hai convogliato ogni frammento nel Flusso dei Frammenti.'''