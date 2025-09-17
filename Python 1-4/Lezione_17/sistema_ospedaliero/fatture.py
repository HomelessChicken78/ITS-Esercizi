from dottore import *
from paziente import *

class Fattura:
    def __init__(self, patient: list[Paziente], doctor: Dottore) -> None:
        if doctor.isAValidDoctor():
            self.__patient = patient
            self.__doctor = doctor
            self.__fatture: int = len(patient)
            self.__salary: int = 0

        else:
            self.__patient = None
            self.__doctor = None
            self.__fatture: int = None
            self.__salary: int = None

    def getSalary(self) -> int: 
        '''deve ritornare il salario guadagnato dal dottore.
        Il salario gudaganto viene calcolato moltiplicando la parcella del dottore per il numero di pazienti.'''

        self.__salary = self.__doctor.getParcel() * len(self.__patient)
        return self.__salary

    def getFatture(self) -> int:
        '''deve assegnare all'attributo fatture il numero di pazienti (in modo che sia sempre aggiornato) che ha il dottore e ritornare il suo valore.'''
        self.__fatture = len(self.__patient)
        return self.__fatture

    def addPatient(self, newPatient: Paziente) -> None:
        '''consente di aggiungere un paziente alla lista di pazienti di un dottore, aggiornando poi il numero di fatture ed il salario,
        richiamando il metodo getFatture() e getSalary(). 
        Stampare "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"'''

        if newPatient not in self.__patient:
            self.__patient.append(newPatient)
            self.getFatture()
            self.getSalary()
            print(f"Alla lista del Dottor {self.__doctor.getLastname()} è stato aggiunto il paziente {newPatient.getidCode()}")
        else:
            print(f"Il paziente è già nella lista del Dottor {self.__doctor.getLastname()}")

    def removePatient(self, idCode) -> None:
        '''consente di rimuovere un paziente alla lista di pazienti di un dottore ricevendo in input il codice identificativo
        del paziente da rimuovere, aggiornando poi il numero di fatture e il salario, richiamando il metodo get Fatture() e getSalary().
        Stampare "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}".'''

        found: bool = False

        for p in self.__patient:
            if p.getidCode() == idCode:
                found = True
                self.__patient.remove(p)
                break
            
        if found == True:
            print(f"Alla lista del Dottor {self.__doctor.getLastname()} è stato rimosso il paziente {idCode}")
        else:
            print(f"Non esiste alcun paziente con codice {idCode} nella lista del Dottor {self.__doctor.getLastname()}")
