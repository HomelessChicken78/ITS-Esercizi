'''Prossimo: Lasciati alle spalle i codici: nel capitolo dei set conterai essenze e incroci.

Censimento delle Essenze
Nelle camere del Conclave dei Set il censimento deve essere perfetto: conta quante scintille sono davvero uniche nel cerchio.
Fallo con `unique_count(nums)`, che restituisce il numero di interi distinti presenti in `nums`.
Mantieni la firma e lascia che i test registrino il tuo conteggio.'''

def unique_count(nums: list[int]) -> int:
    return len(set(nums))

if __name__ == "__main__":
    print(unique_count([2, 3, 4, 4, 4, 2, 4, 1, 2, 9, 0]))

'''Il Conclave ha contato ogni essenza distinta rimasta nel caos: Censimento completato.
Prossimo: Mentre ti rimetti in cammino, il prossimo confronto ti mostrera sfere gemelle da cui estrarre solo cio che condividono.'''