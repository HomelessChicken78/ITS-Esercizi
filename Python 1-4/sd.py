'''
`Scrivere un programma PYTHON che a partire da una stringa la cifra con la tecnica XOR
Successivamente mostrare che la stringa cifrata, riapplicando lo stesso XOR, torna la stringa originale
Per fare lo XOR utilizzate un solo valore: 57
Quindi data la stringa di esempio “Nel mezzo del cammin di nostra vita”, dovete fare per ogni carattere della stringa lo xor con il valore 57
“N” xor 57, “e” xor 57, …
Ottenendo una lista di numeri es: 78 (che è il codice asciii  della lettera N) xor (si indica con il simbolo ^) => 78 ^ 57 = 119
E così via per tutta la stringa.
Al termine stampare la lista di numeri ottenuti
In fondo a partire dalla lista di numeri, riapplicare lo xor sempre con 57 e quindi ottenere (ricostruendola) la stringa originale
NB: potreste utilizzare input(“…”) in modo da leggere sia la stringa da cifrare, sia il valore segreto da applicare come xor
`'''

def xor_cifratura(frase: str, chiave: int) -> list[int]:

    # Senza comprehension
    # res: list[int] = []

    # for carattere in frase:
    #     asciified: int = ord(carattere)

    #     res.append(asciified ^ chiave)

    # Con comprehension
    res: list[int] = [ord(letter)^chiave for letter in frase]

    return res

def xor_decifratura(lista_numeri: list[int], chiave: int) -> list[str]:

    # Senza comprehension
    # res: list[str] = []

    # for numero in lista_numeri:
    #     lettera: int = chr(numero ^ chiave)

    #     res.append(lettera)

    # Con comprehension
    res: list[int] = [chr(numero^chiave) for numero in lista_numeri]

    return res

frase: str = input("frase: ")
chiave: int = int(input("numero: "))

cifrato: list[int] = xor_cifratura(frase, chiave)
decifrato: str = (xor_decifratura(cifrato, chiave))
print(cifrato)
print(''.join(decifrato))