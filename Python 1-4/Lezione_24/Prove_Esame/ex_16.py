'''Scrivi una funzione che converta una lista di tuple (chiave, valore) in un dizionario
 Se la chiave è già presente, aggiungi il valore alla lista di valori già associata alla chiave.'''
# [("a", 1), ("b", 1), ("a", 5)] -> {"a" : [1, 5], "b" : [1]}
def lista_a_dizionario(tuples: list[tuple]) -> dict[str:list[int]]:
    res_dict: dict[str:list[int]] = dict()

    for tuple in tuples:
        if tuple[0] not in res_dict.keys():
            res_dict[tuple[0]] = [tuple[1]]
        else:
            res_dict[tuple[0]].append(tuple[1])
    
    return res_dict

print(lista_a_dizionario([('a', 1), ('b', 2), ('a', 3)]))