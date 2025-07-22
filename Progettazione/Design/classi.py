from typing import Any, Self
import weakref
from Tipi_dati import RealGZ, Index
from datetime import datetime
from abc import ABC, abstractmethod

class Utente(ABC):
    _id_usernames: Index[str, Self] = Index("Lista Username")
    _username: str # <<imm>> {id}
    _registrazione: datetime # <<imm>>

    @abstractmethod
    def __init__(self, username: str, registrazione: datetime):
        if username:
            self._id_usernames.add(username, self)
            self._username = username
        else:
            raise AttributeError("Value for attribute '_username' cannot be None")
        self._registrazione = registrazione
    
    @abstractmethod
    @classmethod
    def all(cls):
        return cls._id_usernames.all()
    
class Privato(Utente):
    def __init__(self, username, registrazione):
        super().__init__(username, registrazione)