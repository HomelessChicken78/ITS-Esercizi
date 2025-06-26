from typing import Self, Any
import re

class IntGE1900(int):
    # Tipo di dato specializzato Intero >= 1900
    def __new__(cls, v: float | int | str | bool | Self) -> Self:
        n: int = super().__new__(cls, v)  # prova a convertire v in un int
        if n >= 1900:
            return n
        raise ValueError(f"Il valore {n} è minore di 1900!")


class IntGEZ(int):
    # Tipo di dato specializzato Intero >= 0 (Greater than or Equal to Zero)
    def __new__(cls, v: float | int | str | bool | Self) -> Self:
        n: int = super().__new__(cls, v)  # prova a convertire v in un int
        if n >= 0:
            return n
        raise ValueError(f"Il valore {n} è minore di 0!")

class FloatGEZ(float):
    # Tipo di dato specializzato Float >= 0 (Greater than or Equal to Zero)
    def __new__(cls, v: float | int | str | bool | Self) -> Self:
        n: float = super().__new__(cls, v)  # prova a convertire v in un float
        if n >= 0:
            return n
        raise ValueError(f"Il valore {n} è minore di 0!")
    
class CodiceFiscale:
    pattern = re.compile(r'^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$')

    def __init__(self, cf: str):
        if not self.is_valid(cf):
            raise ValueError(f"Codice fiscale non valido: {cf}")
        self.cf = cf

    @classmethod
    def is_valid(cls, cf: str) -> bool:
        return bool(cls.pattern.fullmatch(cf))
    
    def __str__(self):
        return self.cf