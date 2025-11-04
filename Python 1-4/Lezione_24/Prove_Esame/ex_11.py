'''Scrivi una funzione che prenda un dizionario e un valore, e ritorni la prima chiave che corrisponde a quel valore, o None se il valore non è presente.'''

def trova_chiave_per_valore(dizionario: dict[str: int], valore: int) -> str:
    for key, searched_value in dizionario.items():
        if searched_value == valore:
            return key
    return None
    
print(trova_chiave_per_valore({'x': 5, 'y': 10, 'z': 15}, 15))