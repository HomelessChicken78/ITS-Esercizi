'''Hai ricevuto una lista di numeri interi, contenente valori compresi tra 1 e n, dove n è la
lunghezza della lista. Tuttavia, alcuni numeri potrebbero mancare: la lista può contenere
duplicati, ma non tutti i numeri da 1 a n sono presenti.

Il tuo compito è individuare i numeri mancanti.

Scrivi una funzione che, data in input una lista, restituisca una nuova lista ordinata
contenente tutti i numeri da 1 a n che non sono presenti nella lista originale.

For example:
print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))
>>>[5, 6]'''

def find_disappeared_numbers(nums: list[int]) -> list[int]:
    minim = min(nums)    #Find the biggest number
    maxim = len(nums)+1    #Find the smallest number

    #create a list containing all the numbers in between them
    missing_nums: list[int] = list(range(minim, maxim))

    #Now remove all the numbers that are already in the original list
    for n in nums:
        if n in missing_nums:
            missing_nums.remove(n)

    return missing_nums


if __name__ == "__main__":
    print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))
    print(find_disappeared_numbers([1,8,9,150]))  #[2, 3, 4]
    print(find_disappeared_numbers([1,8,9,150,9,2189,2,82,3,3,3]))  #[4, 5, 6, 7, 10, 11]