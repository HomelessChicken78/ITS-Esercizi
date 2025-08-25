from abc import ABC, abstractmethod
from string import ascii_lowercase, ascii_uppercase

class CodificatoreMessaggio(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def codifica(testoInChiaro: str) -> None:
        pass

class DecodificatoreMessaggio(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def decodifica(testoCodificato: str) -> None:
        pass

class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, key: int):
        self.key = key

    def codifica(self, testoInChiaro: str) -> str:
        res: str = ""  # This is the result that will be returned

        # Check all letters in the string
        for letter in testoInChiaro:
            if letter in ascii_lowercase:
                alphabet_index: int = ascii_lowercase.index(letter)  # Find what position that the letter has in the alphabet
                # Append to the result the letter that is {self.key} positions ahead. Take into consideration if it goes out of range
                if alphabet_index + self.key > 25:
                    res += ascii_lowercase[(alphabet_index + self.key)%26]
                else:
                    res += ascii_lowercase[alphabet_index + self.key]

            elif letter in ascii_uppercase:
                alphabet_index: int = ascii_uppercase.index(letter)  # Find what position that the letter has in the alphabet
                # Append to the result the letter that is {key} positions ahead. Take into consideration if it goes out of range
                if alphabet_index + self.key > 25:
                    res += ascii_uppercase[(alphabet_index + self.key)%26]
                else:
                    res += ascii_uppercase[alphabet_index + self.key]

            else:
                res += letter

        return res
    
    def decodifica(self, testoCodificato: str) -> str:
            res: str = ""  # This is the result that will be returned

            # Check all letters in the string
            for letter in testoCodificato:
                if letter in ascii_lowercase:
                    alphabet_index: int = ascii_lowercase.index(letter)  # Find what position that the letter has in the alphabet
                    # Append to the result the letter that is {self.key} positions ahead. Take into consideration if it goes out of range
                    if alphabet_index - self.key < 0:
                        res += ascii_lowercase[(alphabet_index - self.key)%26]
                    else:
                        res += ascii_lowercase[alphabet_index - self.key]

                elif letter in ascii_uppercase:
                    alphabet_index: int = ascii_uppercase.index(letter)  # Find what position that the letter has in the alphabet
                    # Append to the result the letter that is {self.key} positions ahead. Take into consideration if it goes out of range
                    if alphabet_index - self.key < 0:
                        res += ascii_uppercase[(alphabet_index - self.key)%26]
                    else:
                        res += ascii_uppercase[alphabet_index - self.key]

                else:
                    res += letter
            
            return res

    def scrivi(self, path: str, text: str) -> None:
        with open(path, "w") as f:
            f.write(text)

    def leggi(self, path: str) -> str:
        with open(path, "r") as f:
            return f.read()

class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):
    def __init__(self, n: int):
        self.n = n
    
    def __dividi_testo(self, string: str) -> tuple[str]:
        lunghezza: int = len(string)
        # Used to split in half the string
        prima_parte: str = string[:lunghezza//2]
        seconda_parte: str = string[lunghezza//2:]

        # Check if they are odd. If they are make it so the first one is longer (still respecting the order)
        if lunghezza % 2 != 0:
            prima_parte += seconda_parte[0]
            seconda_parte = seconda_parte[1:]
        
        return prima_parte, seconda_parte

    def codifica(self, testoInChiaro: str) -> str:
        new_testo: str = testoInChiaro
        for _ in range(self.n):
            prima_parte, seconda_parte = self.__dividi_testo(new_testo)
            new_testo = self.__combinazione(prima_parte, seconda_parte)
        return new_testo
    
    def __combinazione(self, prima: str, seconda: str) -> str:
        res = ""
        for i in range(len(seconda)):
            res += prima[i] + seconda[i]
        
        if len(prima) > len(seconda):
            res += prima[len(prima)-1]
        
        return res

    def decodifica(self, testoCodificato: str) -> str:

        new_testo = testoCodificato
        for _ in range(self.n):
            pari: str = ""
            dispari: str = ""
            for char in range(len(new_testo)):
                if char % 2 == 0:
                    pari += new_testo[char]
                else:
                    dispari += new_testo[char]
            
            new_testo = pari + dispari
        return new_testo
    
    def scrivi(self, path: str, text: str) -> None:
        with open(path, "w") as f:
            f.write(text)

    def leggi(self, path: str) -> str:
        with open(path, "r") as f:
            return f.read()