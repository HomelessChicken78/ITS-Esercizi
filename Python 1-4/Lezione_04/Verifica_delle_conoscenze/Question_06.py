'''La funzione dovrebbe calcolare la media dei numeri in una lista di interi.
Un errore nell'implementazione porta a risultati inaspettati.

Trova l'errore e correggi il codice affinché soddisfi i casi di test.
def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return sum(numbers) / len(numbers)
    else:
        return len(numbers) / sum(numbers) - 1

For example:
print(calculate_average([1, 2, 3, 4, 5]))
>>>3.0

print(calculate_average([]))
>>>0'''

def calculate_average(numbers: list[int]) -> float:
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers)
    
if __name__ == "__main__":
    print(calculate_average([]))