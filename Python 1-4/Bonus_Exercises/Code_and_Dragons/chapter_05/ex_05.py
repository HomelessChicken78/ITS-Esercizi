'''Prossimo: All’ultima sala dei cicli ti vuole pronto a comprimere melodie in sequenze compatte.

Melodia Compressa
L'ultima sala canta note ripetute: devi comprimerle senza perdere il motivo. Intona `rle(s)` per restituire la codifica run‑length
come lista di tuple `(carattere, conteggio)` scorrendo `s`; se `s` è vuota, `[]`. Mantieni la firma e placa i test.'''

def rle(s: str) -> list[tuple[str,int]]:
    if s == "":
        return []
    
    res: list[tuple[str, int]] = []
    current_str: str = ""

    for char in s:
        count: int = 0

        if char not in current_str:
            current_str += char

            for char2 in s:
                if char2 == char:
                    count += 1
            
            res.append((char, count))
    
    return res

print(rle("ciaooa"))

'''La Melodia Compressa risuona nel ponte: ogni nota consecutiva e' annotata. La Melodia Compressa risuona nel ponte: domini il ritmo dei cicli arcani.'''