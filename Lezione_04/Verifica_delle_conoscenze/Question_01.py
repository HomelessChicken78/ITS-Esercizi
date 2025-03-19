'''Scrivi una funzione che, data una lista, ritorni un dictionary che mappa ogni elemento alla sua frequenza nella lista.

print(frequency_dict(['mela', 'banana', 'mela']))
{'mela': 2, 'banana': 1}
'''

def frequency_dict(elements: list) -> dict:
    appearing_elements: list = []

    #This is similar of doing a set, but it keeps the order: originally i did it with a set but it did not work
    for element in elements:
        if element not in appearing_elements:
            appearing_elements.append(element)

    frequencies: dict = {}

    #For every unique existant element (that is in the appearing_elements), count how many of that instance exist in the original list
    for element in appearing_elements:
        frequencies[element] = 0
        for i in elements:
            if i == element:
                frequencies[element] += 1

    return frequencies



if __name__ == "__main__":
 	print(frequency_dict(['a', 'b', 'c', 'a', 'b', 'c', 'a']))