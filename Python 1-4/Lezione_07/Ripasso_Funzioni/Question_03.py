'''
Scrivi una funzione che elimini dalla lista dati certi elementi specificati in un dizionario. Il
dizionario contiene elementi da rimuovere come chiavi e il numero di volte che devono
essere rimossi come valori.
For example:
print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))
>>> [1, 3, 4]

print(rimuovi_elementi([], {2: 1})) 
>>> []
'''

def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    #Take each number it is asked to get removed
    for num in da_rimuovere.keys():
        amount = da_rimuovere[num]  #Take the maximum amount the number has to be removed from the original list

        #Remove all instances of the given number up to a maximum of amount
        while amount > 0:
            #Check if there is at least one "num" in the list. If it is, remove one instance of it.
            if num in lista:
                lista.remove(num)
            amount -= 1

    return lista

if __name__ == "__main__":
    print(rimuovi_elementi([1, 2, 3, 2, 4], {2: 2}))  #[1, 3, 4]
    print(rimuovi_elementi([], {2: 1}))  #[]
    print(rimuovi_elementi([2, 4, 6, 8], {5: 1, 6: 2}))  #[2, 4, 8]