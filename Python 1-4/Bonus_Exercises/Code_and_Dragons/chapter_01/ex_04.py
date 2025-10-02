'''Prossimo: Tra poco ti verra richiesto di scandire il potere in blocchi regolari.

Segmenti Rituali
Gli scribi spettrali pretendono energia scandita in segmenti regolari per il rituale.
Suddividi la sequenza con `chunk(lst, size)`, spezzando `lst` in sottoliste consecutive di lunghezza `size` (l'ultimo blocco può essere più corto).
Mantieni la firma e soddisfa i test.'''

def chunk(lst: list[int], size: int) -> list[list[int]]:
    if not lst:
        return []

    insieme: list[list[int]] = [[]]
    count: int = 0

    for el in lst:
        if count == size:
            insieme.append([])
            count = 0
        insieme[-1].append(el)
        count += 1
    return insieme

if __name__ == "__main__":
    print(chunk([0, 2, 3], 1))

'''Hai scandito i Segmenti Rituali: le colonne seguono il tuo tempo arcano.'''