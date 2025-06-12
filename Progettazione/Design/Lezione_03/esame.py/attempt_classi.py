from __future__ import annotations

class Studente:
    _nome: str # mutable, noto alla nascita
    _esami: set[esame] # mutable, sicuramente non noto alla nascita

    def __init__(self, nome: str):
        self.set_nome(nome)
        self._esami: set[esame] = set()

    def nome(self) -> str:
        return self._nome
    
    def esami(self) -> frozenset[esame]:
        return frozenset(self._esami)

    def set_nome(self, nome) -> None:
        self._nome = nome
    
    def add_esame(self, esame: esame) -> None:
        if esame not in self.esami():
            self._esami.add(esame)
            esame._set_studente(self)
        else:
            raise RuntimeError("L'esame già è presente nella lista di esami dello studente")
    
    def remove_esame(self, esame: esame) -> None:
        if esame in self.esami():
            self._esami.remove(esame)
            esame._set_studente(None)
        else:
            raise RuntimeError("L'esame non è presente nella lista di esami dello studente")
    
    def __str__(self) -> str:
        return f"{self.nome()}"
    
class Modulo:
    _codice: str # immutable, noto alla nascita

    def __init__(self, codice: str):
        self._codice = codice
    
    def codice(self) -> str:
        return self._codice
    
class esame:
    _studente: Studente
    _modulo: Modulo # immutable, certamente non noto alla nascita
    _voto: int # immutable, noto alla nascita

    def __init__(self, modulo: Modulo, voto: int):
        self._studente: Studente = None
        self._modulo: Modulo = modulo
        self._voto: int = voto

    def voto(self) -> int:
        return self._voto

    def _set_studente(self, studente: Studente) -> None:
        self._studente = studente

    def __str__(self) -> str:
        return f"Esame con voto {self._voto}"
    