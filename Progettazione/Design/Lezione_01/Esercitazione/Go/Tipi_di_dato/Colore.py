from enum import *

class Colore(StrEnum):
    bianco = auto()
    nero = auto()

if __name__ == "__main__":
    b = Colore.bianco
    n = Colore.nero

    print(Colore.nero == n)

    color1 = Colore.nero
    color1 = Colore.bianco
    print(color1)