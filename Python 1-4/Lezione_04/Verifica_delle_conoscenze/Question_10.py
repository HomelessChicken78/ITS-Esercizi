'''Scrivi una funzione che unisce due dizionari. Se una chiave è presente in entrambi, somma i loro valori.

For example:
print(merge_dictionaries({'x': 5}, {'x': -5}))
>>>{'x': 0}'''

def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    merged_dict: dict[str, int] = {}
    for k, v in dict1.items():
        merged_dict[k] = v
    
    for k, v in dict2.items():
        if k in merged_dict.keys():
            merged_dict[k] += v
        else:
            merged_dict[k] = v

    return merged_dict

if __name__ == "__main__":
    print("Test 1\n",
          merge_dictionaries({'x': 5}, {'x': -5}))
    print("Test 2\n",
          merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))
    print("Test 3\n",
          merge_dictionaries({}, {'a': 10, 'b': 20}))
    print("Test 4\n",
          merge_dictionaries({'a': 3}, {'b': 4}))