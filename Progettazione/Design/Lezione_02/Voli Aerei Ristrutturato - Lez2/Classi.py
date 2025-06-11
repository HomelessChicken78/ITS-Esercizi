from datetime import timedelta
from Tipi_di_dato import *

class Aeroporto:
    _codice: str  # <<imm>>, noto alla nascita
    _nome: str  # <<mutable>>, noto alla nascita

    def __init__(self, codice: str, nome: str) -> None:
        self._codice = codice
        self.set_nome(nome)

    def nome(self) -> str:
        return self._nome

    def codice(self) -> str:
        return self._codice
 
    def set_nome(self, nome: str) -> None:
        self._nome = nome

class Volo:
    _codice: str  # <<imm>>, noto alla nascita
    _durata_in_minuti: timedelta  # <<mutable>>, noto alla nascita

    def __init__(self, codice: str, durata_in_minuti: IntG0) -> None:
        self._codice = codice
        self.set_durata_in_minuti(durata_in_minuti)

    def codice(self) -> str:
        return self._codice
    
    def durata_in_minuti(self) -> timedelta:
        return self._durata_in_minuti

    def set_durata_in_minuti(self, min: IntG0) -> None:
        self._durata_in_minuti = timedelta(minutes=min)

class CompagniaAerea:
    _nome: str  # <<mutable>>, noto alla nascita
    _fondazione: IntG1900  # <<immutable>>, noto alla nascita

    def __init__(self, nome: str, fondazione: IntG1900) -> None:
        self.set_nome(nome)
        self._fondazione = fondazione

    def nome(self) -> str:
        return self._nome
    
    def fondazione(self) -> IntG1900:
        return self._fondazione
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

class Città:
    _nome: str  # <<mutable>>, noto alla nascita
    _numero_abitanti: IntGE0  # <<mutable>>, noto alla nascita

    def __init__(self, nome: str, numero_abitanti: IntGE0) -> None:
        self.set_nome(nome)
        self.set_numero_abitanti(numero_abitanti)

    def nome(self) -> str:
        return self._nome
    
    def numero_abitanti(self) -> IntGE0:
        return self._numero_abitanti
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def set_numero_abitanti(self, numero: IntGE0) -> None:
        self._numero_abitanti = numero

class Nazione:
    _nome: str  # <<mutable>>, noto alla nascita

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)
    
    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

if __name__ == "__main__":
    # a1: Aeroporto = Aeroporto("adrfiu12418", "Aeroporto di fiumicino")
    # print(a1.codice(), a1.nome())
    # a1.set_nome("Aeroporto Fiumicinese")
    # print(a1.codice(), a1.nome())

    # v1: Volo = Volo("r223adrfmmil39", IntG0(90))
    # print(v1.codice(), v1.durata_in_minuti())
    # v1.set_durata_in_minuti(IntG0(85))
    # print(v1.codice(), v1.durata_in_minuti())

    # Ca1: CompagniaAerea = CompagniaAerea("Ryanr", IntG1900(1984))
    # print(Ca1.nome() + ",", Ca1.fondazione())
    # Ca1.set_nome("Ryanair")
    # print(Ca1.nome() + ",", Ca1.fondazione())

    # c1: Città = Città("Flumicina", IntGE0(0))
    # print(f"{c1.nome()} ha {c1.numero_abitanti()} abitanti.")
    # c1.set_nome("Fiumicino")
    # c1.set_numero_abitanti(IntGE0(83000))
    # print(f"{c1.nome()} ha {c1.numero_abitanti()} abitanti.")

    # Ita: Nazione = Nazione("Italia")
    # print(Ita.nome())
    # Ita.set_nome("Italy")
    # print(Ita.nome())
    pass