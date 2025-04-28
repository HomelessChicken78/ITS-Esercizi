'''

Scrivi una funzione che inverte le chiavi e i valori in un dizionario. Se ci sono valori duplicati, scarta i duplicati.

For example:
print(inverti_mappa({'a': 1, 'b': 2, 'c': 3}))
>>> {1: 'a', 2: 'b', 3: 'c'}

print(inverti_mappa({}))
>>> {}
'''

def inverti_mappa(dizionario: dict[str:int]) -> dict[int:str]:

    #Create a list which contains the keys of the old dictionary. This list will act as the list of values
    values: list[int] = [x for x in dizionario.keys()]

    #Create a list which contains the values of the old dictionary. This list will act as the list of keys
    keys = []
    i = 0
    old_values: list = list(dizionario.values())  #dizionario.values() cannot be subscripted, so i had to use list() to make it subscriptable. However i stored it in a variable to make it easier
    while i < len(old_values):
        #Check if the current value it is trying to append is already in the list "keys" or not. Append it only if it isn't
        if old_values[i] not in keys:
            keys.append(old_values[i])
        
        #If it is duplicate, remove the corresponding value form "values"
        else:
            #Check if it goes out of range
            try:
                values.pop(i)
            #if it does, pop the last value instead
            except IndexError:
                values.pop(len(values)-1)
        
        i += 1

    #Merge "keys" and "values" using a while loop
    inverted_dict: dict[int:str] = {}
    i = 0
    while i < len(keys):
        inverted_dict[keys[i]] = values[i]
        i += 1
    return inverted_dict

if __name__ == "__main__":
    print(inverti_mappa({'a': 3, 'b': 3, 'c': 3}))
    # print(inverti_mappa({'a': 1, 'b': 2, 'c': 3}))  #{1: 'a', 2: 'b', 3: 'c'}
    # print(inverti_mappa({}))  #{}
    # print(inverti_mappa({'a': 1, 'b': 2, 'c': 3, 'd' : 3}))  #{1: 'a', 2: 'b', 3: 'c'}
    # print(inverti_mappa({'a': 1, 'b': 1, 'c': 2}))  #{1: 'a', 2: 'c'}