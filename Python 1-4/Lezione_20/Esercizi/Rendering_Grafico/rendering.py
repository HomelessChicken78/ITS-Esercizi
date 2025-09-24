from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def getArea() -> None:
        '''Calcola l'area'''
        pass

    @abstractmethod
    def render() -> None:
        '''Disegnare su schermo la forma'''
        pass

class Quadrato(Forma):
    def __init__(self, lato: int) -> None:
        super().__init__()
        self.__l: int = lato
    
    def getLato(self) -> int:
        return self.__l

    def getArea(self) -> int:
        return self.getLato() ** 2
    
    def render(self) -> None:
        lenght: int = 1
        height: int = 1

        while height <= self.getLato():
            lenght = 1

            while lenght <= self.getLato():
                if height == 1 or height == self.getLato() or lenght == 1 or lenght == self.getLato(): 
                    print("* ", end="")
                
                else:
                    print("  ", end="")

                lenght += 1
            
            print()
            height += 1

class Rettangolo(Forma):
    def __init__(self, base: int, altezza: int) -> None:
        super().__init__()
        self.__b: int = base
        self.__h: int = altezza
    
    def getBase(self) -> int:
        return self.__b
    
    def getAltezza(self) -> int:
        return self.__h

    def getArea(self) -> int:
        return self.getBase() * self.getAltezza()
    
    def render(self) -> None:
        lenght: int = 1
        height: int = 1

        while height <= self.getAltezza():
            lenght = 1

            while lenght <= self.getBase():
                if height == 1 or height == self.getAltezza() or lenght == 1 or lenght == self.getBase(): 
                    print("* ", end="")
                
                else:
                    print("  ", end="")

                lenght += 1
            
            print()
            height += 1

class Triangolo(Forma):
    def __init__(self, lato: int) -> None:
        super().__init__()
        self.__l: int = lato
    
    def getLato(self) -> int:
        return self.__l

    def getArea(self) -> int:
        return (self.getLato() ** 2) / 2
    
    def render(self) -> None:
        lenght: int = 1
        height: int = 1

        while height <= self.getLato():
            lenght = 1

            while lenght <= height:
                if lenght == 1 or lenght == height or height == self.getLato(): 
                    print("* ", end="")
                
                else:
                    print("  ", end="")

                lenght += 1 
            
            print()
            height += 1

