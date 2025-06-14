from __future__ import annotations
from datetime import date

class Impiegato:
    _nome: str # mutable, noto alla nascita
    _cognome: str # mutable, noto alla nascita
    _data_nascita: date # immutable, certamente noto alla nascita
    _stipendio: float # mutable, noto alla nascita
    _progetti: set[Progetto] # mutable, certamente non noto alla nascita

    def __init__(self, nome: str, cognome: str, data_nascita: date, stipendio: float):
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._data_nascita = data_nascita
        self.set_stipendio(stipendio)
        self._progetti = set()
    
    def nome(self) -> str:
        return self._nome

    def cognome(self) -> str:
        return self._cognome

    def data_nascita(self) -> str:
        return self._data_nascita

    def stipendio(self) -> str:
        return self._stipendio
    
    def progetti(self) -> frozenset[Progetto]:
        return frozenset(self._progetti)
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome
    
    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome
    
    def set_stipendio(self, stipendio: float) -> None:
        self._stipendio = stipendio

    def _add_progetto(self, progetto: Progetto) -> None:
        self._progetti.add(progetto)

    def _remove_progetto(self, progetto: Progetto) -> None:
        self._progetti.remove(progetto)

    def __str__(self) -> str:
        return f"{self.nome()} {self.cognome()}"

class Progetto:
    _nome: str # mutable, noto alla nascita
    _budget: float # mutable, noto alla nascita
    _impiegati: set[Impiegato] # mutable, certamente non noto alla nascita

    def __init__(self, nome: str, budget: float):
        self.set_nome(nome)
        self.set_budget(budget)
        self._impiegati = set()

    def nome(self) -> str:
        return self._nome
    
    def budget(self) -> float:
        return self._budget
    
    def impiegati(self) -> frozenset:
        return frozenset(self._impiegati)
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def set_budget(self, budget: float) -> None:
        self._budget = budget

    def _add_impiegato(self, impiegato: Impiegato) -> None:
        self._impiegati.add(impiegato)

    def _remove_impiegato(self, impiegato: Impiegato) -> None:
        self._impiegati.remove(impiegato)

    def __str__(self) -> str:
        return f"{self.nome()} {self.budget()}"

class partecipa:
    _impiegato: Impiegato
    _progetto: Progetto
    _data: date

    def __init__(self, impiegato: Impiegato, progetto: Progetto, data: date):
        self._impiegato: Impiegato = impiegato
        impiegato._add_progetto(progetto)

        self._progetto: Progetto = progetto
        progetto._add_impiegato(impiegato)

        self._data = data
    
    def data(self) -> date:
        return self._data
    
    # MODELLARE IL FATTO CHE OGGETTO DI CLASSE A E OGGETTO DI CLASSE B NON POSSONON ESSER COINVOLTI IN DUE LINK DELL'ASSOCIAZIONE A-B
    ...