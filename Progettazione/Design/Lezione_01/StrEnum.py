from enum import *

class Gender(StrEnum):
    Uomo = auto()
    Donna = auto()

a = Gender.Donna
print(a)