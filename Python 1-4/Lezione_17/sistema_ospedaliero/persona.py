'''### CLASSE PERSONA'''

class Persona:
    __first_name: str
    __last_name: str
    __age: int

    def __init__(self, first_name, last_name):
        self.setAge(0)

        self.setName(first_name)
        
        self.setLastName(last_name)
    
    def setName(self, first_name: str) -> None:
        '''consente di impostare il nome di una persona, modificando il valore del relativo attributo. 
        Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, 
        ad esempio "Il nome inserito non è una stringa!".'''

        if not isinstance(first_name, str):
            first_name = ""
            print("Il nome inserito non è una stringa!")
            self.setAge(None)
        self.__first_name = first_name

    def setLastName(self, last_name: str) -> None:
        '''consente di impostare il cognome di una persona, modificando il valore del relativo attributo. 
        Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, 
        ad esempio "Il cognome inserito non è una stringa!".'''
        
        if not isinstance(last_name, str):
            last_name = ""
            print("Il cognome inserito non è una stringa!")
            self.setAge(None)
        self.__last_name = last_name
    
    def setAge(self, age: int) -> None:
        if isinstance(age, int) or age is None:
            self.__age = age
        else:
            print("L'età deve essere un numero intero!")

    def getName(self) -> str:
        '''consente di ritornare il nome di una persona.'''
        return self.__first_name

    def getLastname(self) -> str:
        '''consente di ritornare il cognome di una persona.'''
        return self.__last_name

    def getAge(self) -> int:
        '''consente di ritornare l'età di una persona.'''
        return self.__age

    def greet(self) -> None:
        '''stampa il seguente saluto "Ciao, sono {nome} {cognome}! Ho {età} anni!"'''
        print(f"Ciao, sono {self.getName()} {self.getLastname()}! Ho {self.getAge()} anni!")