from film import Film
from movie_genre import *

class Noleggio:
    __film_list: list[Film]
    __rented_film: dict[int, list[Film]]

    def __init__(self, film_list: list[Film]) -> None:
        self.__film_list: list[Film] = film_list
        self.__rented_film: dict[int, list[Film]] = dict()

    def isAvailable(self, film: Film) -> bool: 
        '''tale metodo deve ritornare True se il film passato come argomento è presente nell'inventario del negozio, false
        in caso contrario.
        Se il film è disponibile in negozio da un messaggio di conferma.
        Se il film non è disponibile stampa un messaggio di errore'''

        if film in self.__film_list:
            print(f"Il film scelto è disponibile: {film.getTitle()}!")
            return True
        else:
            print(f"Il film scelto non è disponibile al momento: {film.getTitle()}!")
            return False
        
    def rentAMovie(self, film: Film, clientID: int) -> None:
        '''tale metodo deve gestire il noleggio di un film.
        Affinché sia possibile noleggiare un film, un film deve essere disponibile in negozio.
        Pertanto, il metodo deve verificare la disponibilità. Nel caso in cui il film richiesto sia disponibile, rimuoverlo dalla lista dei film
        disponibili in negozio, poi riempire il dizionario rented_film in questo modo:
            la chiave sarà l'id del cliente che noleggia (id_client)
            il corrispondente valore sarà una lista contenente i film noleggiati da quel cliente.
        Pertanto, il film noleggiato, una volta rimosso dalla lista dei film disponibili in negozio deve essere aggiunto alla lista dei film noleggiati
        dal cliente dato.
        Se il cliente ha potuto noleggiare il film richiesto, stampare:
        "Il cliente {clientId} ha noleggiato {titolo_film}!".
        Se, invece, il film richiesto non è disponibile pe il noleggio, stampare:
        "Non è possibile nolegiare il film {titolo_film}!".'''

        if self.isAvailable(film):
            self.__film_list.remove(film)

            if clientID in self.__rented_film.keys():
                self.__rented_film[clientID].append(film)
            else:
                self.__rented_film[clientID] = [film]

            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
        
        else:

            print(f"Non è possibile nolegiare il film {film.getTitle()}")

    def giveBack(self, film: Film, clientID: int, days: int) -> None:
        '''questo metodo consente di restituire un film noleggiato in negozio. 
        Il film da restituire deve essere rimosso dalla lista dei film noleggiati dal cliente con id clientID, e tale film, deve essere riaggiunto alla
        lista dei film disponibili in negozio (film_list). Successivamente, il metodo deve calcolare la penale che il cliente deve pagare utilizzando
        l'opposito metodo.
        Stampare la penale che il cliente deve pagare:
        "Cliente: {clientID}! La penale da pagare per il film {titolo_film} e' di {tot} euro!".'''

        # Controlla che il cliente esista
        if clientID in self.__rented_film.keys():

            # Controlla che quel cliente abbia quel film
            if film in self.__rented_film[clientID]:
                self.__rented_film[clientID].remove(film)
                self.__film_list.append(film)

                print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} e' di {film.calcolaPenaleRitardo(days)} euro!")
            
            else:
                print(f"Il cliente {clientID} non ha in noleggio quel film!")

        else:
            print(f"Non esiste alcun cliente con codice {clientID} nei registri!")

    def printMovies(self) -> None:
        '''stampa la lista di tutti i film disponibili in negozio.'''
        for f in self.__film_list:
            print(f"{f.getTitle()} - {f.getGenere()}")
    
    def printRentMovies(self, clientID: int) -> None:
        '''questo metodo deve stampare la lista dei film noleggiati dal cliente di cui viene specificato l'id.'''
        
        # Controlla che il cliente esista
        if clientID in self.__rented_film.keys():
            for f in self.__rented_film[clientID]:
                print(f"{f.getTitle()} - {f.getGenere()}")

        else:
            print(f"Non esiste alcun cliente con codice {clientID} nei registri!")