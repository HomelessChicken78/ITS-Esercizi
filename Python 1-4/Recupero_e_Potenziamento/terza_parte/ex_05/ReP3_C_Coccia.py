from random import randint

class Creatura:
    __nome: str

    def __init__(self, nome: str):
        self.setNome(nome)
    
    def setNome(self, nome: str) -> None:
        from string import punctuation

        valid: bool = True

        if isinstance(nome, str):
            for carattere in nome:
                if carattere in punctuation and carattere != "-":
                    valid = False
                    break
        else:
            valid = False
        
        self.__nome = nome if valid else "Creatura Generica"
    
    def nome(self) -> str:
        return self.__nome
    
    def __str__(self) -> str:
        return f"Creatura: {self.nome()}"

class Alieno(Creatura):
    __matricola: int # Positivo
    __munizioni: list[int] # 15 interi positivi

    def __init__(self, nome: str):
        self.__setMatricola()
        self.__setMunizioni()

        if nome == "Robot-"+str(self.matricola()):
            super().__init__(nome)
        else:
            print("Attenzione! Tutti gli Alieni devono avere il nome \"Robot\" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
            super().__init__("Robot-"+str(self.matricola()))

    def __setMatricola(self) -> None:
        self.__matricola = randint(10000, 90000)

    def __setMunizioni(self) -> None:
        self.__munizioni = [n*n for n in range(0,16)]
    
    def matricola(self) -> int:
        return self.__matricola
    
    def munizioni(self) -> list[int]:
        return self.__munizioni

    def __str__(self) -> str:
        return f"Alieno: {self.nome()}"

class Mostro(Creatura):
    __urlo_vittoria: str
    __gemito_sconfitta: str
    __assalto: list[int] # 15 interi positivi

    def __init__(self, nome: str, urlo_vittoria: str, gemito_sconfitta: str):
        super().__init__(nome)

        self.__setVittoria(urlo_vittoria)
        self.__setSconfitta(gemito_sconfitta)

        self.__setAssalto()

    def __setAssalto(self) -> None:
        l: list[int] = []
        for i in range(0, 15):
            rand_num: int = randint(1,100)

            while rand_num in l:
                rand_num = randint(1, 100)

            l.append(rand_num)
    
        self.__assalto = l
    
    def assalto(self) -> list[int]:
        return self.__assalto
    
    def __setVittoria(self, vittoria: str) -> str:
        valid: bool = True

        for carattere in vittoria:
            if carattere.isnumeric():
                valid = False
                break
        
        self.__urlo_vittoria = vittoria if valid else "GRAAAHHH"

    def __setSconfitta(self, sconfitta: str) -> str:
        valid: bool = True

        for carattere in sconfitta:
            if carattere.isnumeric():
                valid = False
                break
        
        self.__gemito_sconfitta= sconfitta if valid else "Uuurghhh"
    
    def vittoria(self) -> str:
        return self.__urlo_vittoria
    
    def sconfitta(self) -> str:
        return self.__gemito_sconfitta
    
    def __str__(self) -> str:
        res: str = ""
        minuscola: bool = True

        for carattere in self.nome():
            if minuscola:
                res += carattere.lower()
                minuscola = False
            else:
                res += carattere.upper()
                minuscola = True
        
        return f"Mostro: {res}"

def listaPositiva(lst: list[int]) -> bool:
    '''Ritorna True se tutti i numeri nella lista sono positivi o 0'''
    for element in lst:
        if element < 0:
            return False
    return True

def pariUguali(a: list[int], b: list[int]) -> list[int]:
    '''Questo metodo riceve in input due liste a e b di interi positivi e deve 
    estituire una lista c.

    Ogni elementi della lista c deve essere uguale a:
    - 1 se l'elemento i-esimo di a e l'elemento i-esimo di b sono sono entrambi pari
    - 0 altrimenti'''
    if not (listaPositiva(a) and listaPositiva(b)):
        raise ValueError("Le liste devono avere valori positivi!")
    
    # Find the longest list
    if len(a) >= len(b):
        longest_list: list[int] = a
        shortest_list: list[int] = b
    else:
        longest_list: list[int] = b
        shortest_list: list[int] = a
    
    c: list[int] = []
    index: int = 0

    while index < len(shortest_list):
        if shortest_list[index] % 2 == 0 and longest_list[index] % 2 == 0:
            c.append(1)
        else:
            c.append(0)
        index += 1
    
    for i in range(0, ((len(longest_list)-1)-index)+1):
        c.append(0)

    return c

def combattimento(a: Alieno, m: Mostro) -> None|Alieno|Mostro:
    '''Questo metodo riceve in input un oggetto della classe Alieno ed un oggetto della
    classe Mostro. Il metodo deve controllare la validità di a e la validità di m. Se a non è un Alieno o se m non è un
    Mostro, il combattimento deve essere interrotto, mostrare un opportuno messaggio e ritornare None. Altrimenti, se a e
    m sono oggetti validi, il metodo deve simulare il combattimento tra Mostro e Alieno, restituendo la creatura vincitrice.
    Il combattimento consiste nell'applicare la funzione pariUguali() alle munizioni dell'Alieno e all'assalto del Mostro.
    Se la lista prodotta in output dal pariUguali() ha più di 4 elementi con valore 1, allora il vincitore è il mostro.
    Altrimenti, il vincitore è l'alieno. Se vince il mostro, sullo schermo viene stampato per 3 volte l'urlo della vittoria,
    altrimenti viene stampato il gemito della sconfitta.'''

    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        print("Combattenti non validi. Uno deve essere un Mostro e l'altro un Alieno!")
        return
    
    simulate: list[int] = pariUguali(a.munizioni(), m.assalto())
    ones: int = 0

    for num in simulate:
        if num == 1:
            ones += 1
    
    if ones >= 4:
        print((m.vittoria()+"\n")*3, end="")
        return m
    else:
        print(m.sconfitta())
        return a

def proclamaVincitore(c: Creatura) -> None:
    if isinstance(c, Mostro):
        print("I Mostri hanno vinto!")
    elif isinstance(c, Alieno):
        print("Gli Alieni hanno vinto!")

    print()
    for i in range(0, 6):
        for j in range(0, len(c.__str__())+10):
            if i == 0 or i == 5:
                print("*", end="")
            elif i == 2 and j == 5:
                print(c, end="")
                print("    *", end="")
                break
            elif j == 0 or j == len(c.__str__())+9:
                print("*", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    # c1: Creatura = Creatura("Blob")
    # print(c1)
    # c1.setNome("11!!!!")
    # print(c1)
    # c1.setNome(123)
    # print(c1)

    a1: Alieno = Alieno("Robot-2")
    print(a1)
    print(a1.matricola())
    print(a1.munizioni())

    print()
    m1: Mostro = Mostro("Godzilla", "GRAHR", "NOOOOO")
    print(m1)
    print(m1.assalto())
    print(m1.vittoria())
    print(m1.sconfitta())

    # print(pariUguali([0, 1], [0, 1, 2, 3, 4]))
    # print(pariUguali([-1], [-2]))

    print()
    # combattimento(1, "Sono un alieno")
    proclamaVincitore(combattimento(a1, m1))