from typing import Self

class Film:
    __id: int
    __title: str

    def __init__(self, id: int, title: str) -> None:
        self.setID(id)
        self.__title: str = title

    def setID(self, id: int) -> None:
        '''consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.'''
        self.__id = id
    
    def setTitle(self, title: str) -> None:
        '''consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.'''
        self.__title = title
    
    def getID(self) -> int:
        '''consente di ritornare il valore del codice identificativo di un film.'''
        return self.__id

    def getTitle(self) -> str:
        '''consente di ritornare il valore del titolo di un film.'''
        return self.__title

    def isEqual(self, otherFilm: Self) -> bool:
        '''ritorna true se il codice identificativo di due film è uguale.'''
        return self.getID() == otherFilm.getID()

