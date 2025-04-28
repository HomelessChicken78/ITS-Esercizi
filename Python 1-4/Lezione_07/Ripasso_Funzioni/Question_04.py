'''
Scrivi una funzione che prenda in input una lista di dizionari che rappresentano voti di studenti e aggrega i voti per studente in un nuovo dizionario.

For example:
print(aggrega_voti([{'nome': 'Alice', 'voto': 90}, {'nome': 'Bob', 'voto': 75}, {'nome': 'Alice', 'voto': 85}]))
>>> {'Alice': [90, 85], 'Bob': [75]}

print(aggrega_voti([])) 
>>> {}'''

def aggrega_voti(voti: list[dict]) -> dict[str:list[int]]:
    res_dict: dict[str:list[int]] = {}

    for diz in voti:
        name: str = diz['nome']
        #Create a key for each name you find. If the list already exist, because it is the second time it appears, skip this
        #Why? Because else it would "reset" the list each time it finds it
        if name not in res_dict:
            res_dict[name] = []

        #Fill in each sub-list
        res_dict[name].append(diz['voto'])

    return res_dict

if __name__ == "__main__":
    print(aggrega_voti([
        {'nome': 'Alice', 'voto': 90},
        {'nome': 'Bob', 'voto': 75},
        {'nome': 'Alice', 'voto': 85}
        ]))
    #>>> {'Alice': [90, 85], 'Bob': [75]}

    print(aggrega_voti([]))  #{}

    print(aggrega_voti([{'nome': 'Alice', 'voto': 100}]))  #{'Alice': [100]}

    print(aggrega_voti([
        {'nome': 'Bob', 'voto': 75},
        {'nome': 'Bob', 'voto': 85}
        ]))
    #>>> {'Bob': [75, 85]}

    print(aggrega_voti([
        {'nome': 'Carl', 'voto': 60},
        {'nome': 'Carl', 'voto': 70},
        {'nome': 'Carl', 'voto': 80}
        ]))
    #>>> {'Carl': [60, 70, 80]}