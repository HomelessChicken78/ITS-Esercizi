from persona import *

class Paziente(Persona):
    def __init__(self, first_name: str, last_name: str, code: str):
        super().__init__(first_name, last_name)

        self.setIdCode(code)
    
    def setIdCode(self, idCode) -> None:
        '''consente di impostare il codice identificativo del paziente.'''
        self.__code = idCode

    def getidCode(self) -> str:
        '''consente di ritornare il codice identificativo del paziente.'''
        return self.__code

    def patientInfo(self) -> None:
        '''stampa in output le informazioni del paziente '''
        print(f"Paziente: {self.getName()} {self.getLastname()}\nID: {self.getidCode()}")