'''Prossimo: Mentre avanzi, prepara le mappe: dovrai fondere atlanti rivali conservando gli aggiornamenti piu freschi.

Atlante Fuso
Due atlanti rivali scintillano sul leggio: fondi le mappe tenendo solo le rune più recenti.
Compila `merge_overwrite(a, b)` per restituire un nuovo dizionario dove i valori di `a` sono sovrascritti dagli aggiornamenti in `b`.
Mantieni la firma e appaga i test.'''

def merge_overwrite(a: dict, b: dict) -> dict:
    result_dict: dict = a.copy()

    for k, v in b.items():
        result_dict[k] = v

    return result_dict

'''Gli atlanti rivali condividono ora rune coerenti: Atlante Fuso completato.'''