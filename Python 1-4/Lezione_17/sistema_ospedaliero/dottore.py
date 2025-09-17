from persona import *

class Dottore(Persona):
    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float):
        super().__init__(first_name, last_name)
        
        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            self.__specialization = None
            print("La specializzazione inserita non è una stringa!")

        if isinstance(parcel, int|float):
            self.__parcel = float(parcel)
        else:
            self.__parcel = None
            print("La parcella inserita non è un float!")

    def setSpecialization(self, specialization: str) -> None:
        '''consente di impostare la specializzazione di un dottore, modificando il valore del relativo attributo.
        Il valore viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stamapre un messaggio di errore, ad esempio
        "La specializzazione inserita non è una stringa!".'''

        if isinstance(specialization, str):
            self.__specialization = specialization
        else:
            print("La specializzazione inserita non è una stringa!")

    def setParcel(self, parcel: float) -> None:
        '''consente di impostare la parcella di un dottore, modificando il valore del relativo attributo.
        Il valore viene modificato se e solo se viene passato al metodo un float. In caso contrario, stamapre un messaggio di errore, ad esempio
        "La parcella inserita non è un float!".'''


        if isinstance(parcel, int|float):
            self.__parcel = float(parcel)
        else:
            print("La parcella inserita non è un float!")

    def getSpecialization(self) -> str:
        '''consente di ritornare la specializzazione del dottore.'''
        return self.__specialization

    def getParcel(self) -> float: 
        '''consente di ritornare la parcella del dottore.'''
        return self.__parcel

    def isAValidDoctor(self) -> bool: 
        '''stabilisce se un dottore è un dottore valido; un dottore è valido se e solo se ha più di 30 anni, in quanto ha avuto il tem-
        po necessario di compiere i suoi studi in medicina. Stampare "Doctor nome e cognome is valid!", se il dottore risulta valido. In caso contrario,
        stampare "Doctor nome e cognome is not valid!".'''
        if self.getAge() >= 30:
            print(f"Doctor {self.getName()} {self.getLastname()} is valid!")
            return True
        print(f"Doctor {self.getName()} {self.getLastname()} is not valid!")
        return False

    def doctorGreet(self) -> None: 
        '''tale metodo richiama la funzione greet() della classe Persona. Poi, stampa il seguente saluto "Sono un medico {specializzazione}"'''
        self.greet()
        print(f"Sono un medico {self.getSpecialization()}")