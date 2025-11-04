'''Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.'''

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    res: dict = dict1.copy()

    if not dict1:
        return dict2
    
    if not dict2:
        return dict1
    
    for k, v in dict2.items():
        if k in res:
            res[k] += v
        
        else:
            res[k] = v
    
    return res

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})) # {'a': 1, 'b': 5, 'c': 4}
