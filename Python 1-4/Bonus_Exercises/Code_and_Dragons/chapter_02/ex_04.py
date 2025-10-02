'''Prossimo: Mentre ti rimetti in cammino, il prossimo rituale ti sommergera di lettere da contare con precisione alchemica.

Pioggia di Lettere
Una pioggia di lettere si stacca dal soffitto: conta i sussurri autentici ignorando il rumore delle luci e del metallo.
Invoca `letter_count(text)` per restituire un dizionario con le occorrenze delle sole lettere alfabetiche, convertite in minuscolo,
ignorando tutto il resto. Mantieni la firma e soddisfa i test.'''

def letter_count(text: str) -> dict[str,int]:
    letters: dict[str] = dict()

    for char in text.lower():
        if char in "abcdefghijklmnopqrstuvxyz":
            if char in letters.keys():
                letters[char] += 1
            else:
                letters[char] = 1
    
    return letters

'''Hai contato ogni lettera arcana nel diluvio: Pioggia di Lettere domata.'''