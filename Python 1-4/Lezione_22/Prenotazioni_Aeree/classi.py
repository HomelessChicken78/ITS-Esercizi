from abc import ABC, abstractmethod

class Volo(ABC):
    _codice_volo: str
    _max_posti: int
    _prenotazioni: int

    @abstractmethod
    def __init__(self, codice_volo: str, max_posti: int):
        self._codice_volo = codice_volo
        if max_posti < 0:
            raise ValueError("Non è possibile inserire un numero di posti inferiore a 0")
        self._max_posti = max_posti
        self._prenotazioni = 0
    
    @abstractmethod
    def codice_volo(self) -> str:
        return self._codice_volo
    
    @abstractmethod
    def max_posti(self) -> int:
        return self._max_posti
    
    @abstractmethod
    def prenota_posto(self) -> None:
        pass

    @abstractmethod
    def posti_disponibili(self) -> None:
        pass

class VoloCommerciale(Volo):
    _posti_economia: int
    _posti_business: int
    _posti_prima: int
    _prenotazioni_economica: int
    _prenotazioni_business: int
    _prenotazioni_prima: int

    def __init__(self, codice_volo: str, max_posti: int):
        super().__init__(codice_volo, max_posti)

        self._posti_economia = round(self.max_posti() * 0.7)
        self._posti_business = round(self.max_posti() * 0.2)
        self._posti_prima = self.max_posti() - (self.posti_economia() + self.posti_business())

        self._prenotazioni_economica = 0
        self._prenotazioni_business = 0
        self._prenotazioni_prima = 0
    
    def codice_volo(self) -> str:
        return self._codice_volo
    
    def max_posti(self) -> int:
        return self._max_posti
    
    def prenota_posto(self, posti: int, classe_servizio: str) -> None:
        '''Consente di prenotare un certo numero di posti sul volo in
        una determinata classe. Tale metodo, prima di riservare un posto, deve controllare prima che ci siano
        posti disponibili sull'intero volo, poi se ci sono posti disponibili nella classe richiesta. In caso
        affermativo, contare il numero dei posti prenotati in tale classe. Inoltre, nel caso in cui sia possibile
        prenotare un posto, il metodo deve stampare a schermo un messaggio che notifichi all'utente di aver
        riservato un tot di posti per una determinata classe su un dato volo (specificando il codice del volo).
        In caso contrario, stampare a schermo un messaggio che notifichi all'utente che non ci sono più posti
        disponibili nella classe scelta. Se sul volo non ci sono più posti disponibili, il metodo deve stampare a
        schermo un messaggio notificando all'utente che il volo è al completo. Inoltre, se la classe passata come
        input del metodo non risulta essere una delle seguenti classi ("economica", "business", "prima"), il metodo
        deve stamapre a schermo un messaggio di errore, notificando all'utente che la classe richiesta non è valida.
        Infine, il metodo deve aggiornare l'attributo prenotazioni della classe estesa Volo, sommando il numero di
        prenotazioni ricevute per ogni classe di servizio, poi aggiornare gli attributi prenotazioni_economica,
        prenotazioni_business, prenotazioni_prima con l'esatto numero delle prenotaioni ricevute per ogni classe di servizio.
        Suggerimento: introdurre delle variabili locali d'appoggio per gestire le prenotazioni per ogni classe di servizio
        da azzerare all'inizio di ogni fase di prenotazione.'''

        disponibili: dict[str, int] = self.posti_disponibili() # Alias
        pronome: str = "o" if posti == 1 else "i"
        #"economica", "business", "prima"
        if disponibili["posti disponibili"] > 0:
            match classe_servizio.lower():
                case "economica":
                    if disponibili["classe economica"] - posti >= 0:
                        self._prenotazioni += posti
                        self._prenotazioni_economica += posti
                        print(f"{posti} posti prenotat{pronome} su {self.codice_volo()} in classe {classe_servizio}.")
                    else:
                        print(f"Non è possibile riservare {posti} post{pronome} in classe {classe_servizio}. Numero posti disponibili: {disponibili['classe economica']}")
                
                case "business":
                    if disponibili["classe business"] - posti >= 0:
                        self._prenotazioni += posti
                        self._prenotazioni_business += posti
                        print(f"{posti} posti prenotat{pronome} su {self.codice_volo()} in classe {classe_servizio}.")
                    else:
                        print(f"Non è possibile riservare {posti} post{pronome} in classe {classe_servizio}. Numero posti disponibili: {disponibili['classe business']}")
                    
                case "prima":
                    if disponibili["prima classe"] - posti >= 0:
                        self._prenotazioni += posti
                        self._prenotazioni_prima += posti
                        print(f"{posti} posti prenotat{pronome} su {self.codice_volo()} in classe {classe_servizio}.")
                    else:
                        print(f"Non è possibile riservare {posti} post{pronome} in classe {classe_servizio}. Numero posti disponibili: {disponibili['prima classe']}")

                case _:
                    print("La classe richiesta non è valida.")
        else:
            print(f"Volo {self.codice_volo()} al completo!")

    def posti_disponibili(self) -> dict[str, int]:
         ''' Ritorna un dizionario in cui vengono salvati il numero di posti
        disponibili totali sul volo nel seguente modo: il dizionario deve avere quattro chiavi, ovvero,
        'posti disponibili', 'classe economica', 'classe business', 'prima classe'. Alla chiave
        'posti disponibili' associare come rispettivo valore il numero di posti disponibili rimasti sul
        volo, alla chiave 'classe economica' associare come rispettivo valore il numero di posti che sono
        rimasti disponibili nella classe economica, alla chiave 'classe business' associare come rispettivo
        valore il numero di posti che sono rimasti disponibili nella classe business, alla chiave 'prima classe'
        associare come rispettivo valore il numero di posti che sono rimasti disponibili nella prima classe.
        Se i posti disponibili sia sul volo, sia su una specifica classe di servizio sono esauriti, il valore
        da associare alla corrispondete chiave è 0.'''

         return {'posti disponibili' : self.max_posti()-self._prenotazioni,
                 'classe economica' : self.posti_economia()-self._prenotazioni_economica,
                 'classe business' : self.posti_business()-self._prenotazioni_business,
                 'prima classe' : self.posti_prima()-self._prenotazioni_prima}

    def posti_economia(self) -> int:
        return self._posti_economia

    def posti_business(self) -> int:
        return self._posti_business
    
    def posti_prima(self) -> int:
        return self._posti_prima
   
class VoloCharter(Volo):
    _costo: float

    def __init__(self, codice_volo: str, max_posti: int, costo: float):
        super().__init__(codice_volo, max_posti)
        self._costo = costo
    
    def codice_volo(self) -> str:
        return self._codice_volo
    
    def max_posti(self) -> int:
        return self._max_posti
    
    def costo(self) -> float:
        return self._costo
    
    def prenota_posto(self) -> None:
        if self.posti_disponibili() == self.max_posti():
            self._prenotazioni = self.max_posti()
            print(f"Volo charter {self.codice_volo()} prenotato completamente per {self.costo() * self.max_posti():.2f}€")
        else:
            print(f"Il volo charter {self.codice_volo()} è gia prenotato.")

    def posti_disponibili(self) -> dict[str, int]:
        return self.max_posti() - self._prenotazioni
    
'''
Classe CompagniaAerea:
Questa classe deve avere un costruttore che richiede come argomento in input solo il nome della compagnia (stringa)
ed il prezzo standard di un biglietto (numero float), e creare una lista vuota chiamata flotta.
La classe CompagniaAerea deve gestire molteplici voli commerciali, attraverso i seguenti metodi:
    '''

class CompagniaAerea:
    _nome: str
    _prezzo: float
    _flotta: list[VoloCommerciale]

    def __init__(self, nome: str, prezzo: float):
        self.set_nome(nome)
        self._prezzo = prezzo
        self._flotta: list[VoloCommerciale] = []

    def nome(self) -> str:
        return self._nome
    
    def prezzo(self) -> float:
        return self._prezzo
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def aggiungi_volo(self, volo_commerciale: VoloCommerciale) -> None:
        if not isinstance(volo_commerciale, VoloCommerciale):
            print(f"Il volo inserito non è un Volo Commerciale!")
            
        elif volo_commerciale in self._flotta:
            print(f"Il volo è già presente nella flotta della compagnia aerea {self.nome()}")

        else:
            self._flotta.append(volo_commerciale)
    
    def rimuovi_volo(self, volo_commerciale: VoloCommerciale) -> None:
        if not isinstance(volo_commerciale, VoloCommerciale):
            print(f"Il volo inserito non è un Volo Commerciale!")
            
        elif volo_commerciale not in self._flotta:
            print(f"Il volo non è presente nella flotta della compagnia aerea {self.nome()}")

        else:
            self._flotta.remove(volo_commerciale)

    def mostra_flotta(self) -> None:
        print(f"Ecco la flotta della compagnia aerea {self.nome()}:")
        for volo in self._flotta:
            print(f"volo commerciale {volo.codice_volo()}")
    
    def guadagno(self) -> float:
        # return float(f"{len(self._flotta) * self.prezzo():.2f}")
        tot: int = 0

        for volo in self._flotta:
            tot += volo._prenotazioni_economica * self.prezzo()
            tot += volo._prenotazioni_business * self.prezzo() * 2
            tot += volo._prenotazioni_prima * self.prezzo() * 3
        
        return float(f"{tot:.2f}")



