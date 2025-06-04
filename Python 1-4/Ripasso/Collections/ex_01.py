'''
1) Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario. Se
la chiave è già presente, somma il valore al valore già associato alla chiave.
'''
# [("ciao", 4), ("ciao2", 43)] -> {"ciao" : 4, "ciao2" : 43}

from typing import Any

def from_list_tuple_to_dict(ls: list[tuple[Any, Any]]) -> dict[Any, Any]:
    # Soluzione 1 - Più lunga ma gestibile a proprio piacimento e comprensibile
    res: dict = {}

    for tupl in ls:
        key, value = tupl[0], tupl[1]
        if key in res:
            res[key] += value
        else:
            res[key] = value
    
    return res

    # Soluzione 2 - Più corta e semplice, ma non permette di gestire bene il caso in cui ci siano chiavi duplicate
   #return dict(ls)

if __name__ == "__main__":
    print(from_list_tuple_to_dict([("ciao", 4), ("ciao2", 43)]))