from film import Film

class Azione(Film):
    def __init__(self, id: int, title: str):
        super().__init__(id, title)
        self.__genere: str = "Azione"
        self.__penale: float = 3.00
    
    def getGenere(self) -> str:
        '''ritorna il genere di film'''
        return self.__genere
    
    def getPenale(self) -> float:
        '''ritorna il valore della penale'''
        return self.__penale
    
    def calcolaPenaleRitardo(self, days: int) -> float:
        '''che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.'''
        return self.__penale * days
    
class Commedia(Film):
    def __init__(self, id: int, title: str):
        super().__init__(id, title)
        self.__genere: str = "Commedia"
        self.__penale: float = 2.50
    
    def getGenere(self) -> str:
        '''ritorna il genere di film'''
        return self.__genere
    
    def getPenale(self) -> float:
        '''ritorna il valore della penale'''
        return self.__penale
    
    def calcolaPenaleRitardo(self, days: int) -> float:
        '''che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.'''
        return self.__penale * days

class Drama(Film):
    def __init__(self, id: int, title: str):
        super().__init__(id, title)
        self.__genere: str = "Drama"
        self.__penale: float = 2.00
    
    def getGenere(self) -> str:
        '''ritorna il genere di film'''
        return self.__genere
    
    def getPenale(self) -> float:
        '''ritorna il valore della penale'''
        return self.__penale
    
    def calcolaPenaleRitardo(self, days: int) -> float:
        '''che prende in ingresso il numero dei giorni di ritardo per un film e restituisce la penale da pagare per quel film.'''
        return self.__penale * days