'''Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.'''

def frequency_dict(elements: list) -> dict:
    res: dict = dict()
    
    for el in elements:
        tot = 0

        if el not in res:
            for elem in elements:
                if elem == el:
                    tot += 1
        
            res[el] = tot
    
    return res