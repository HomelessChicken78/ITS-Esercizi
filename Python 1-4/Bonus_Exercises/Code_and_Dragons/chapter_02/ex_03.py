'''Prossimo: Si avvicina la prova in cui invertirai stemmi e alleanze senza confonderli.

Alleanze Invertite
Gli stemmi degli arconti chiedono inversioni fedeli: ogni simbolo ritrovi il proprio portatore.
Esegui `invert_unique(d)`, che inverte chiavi e valori assumendo valori univoci. Mantieni la firma e compiaci i test.'''

def invert_unique(d: dict) -> dict:
    result_dict: dict = dict()
    
    for k, v in d.items():
        result_dict[v] = k

    return result_dict

'''Gli stemmi degli arconti scambiano fedelta con precisione: Alleanze Invertite eseguite.'''