class Movie:
    _ids: list[str] = []

    def __init__(self, movie_id: str, title: str, director: str) -> None:
        if movie_id in Movie._ids:
            raise ValueError(f"Esiste già un film con id \"{movie_id}\"")
        self.movie_id = movie_id
        Movie._ids.append(movie_id)

        self.title = title
        self.director = director
        self.is_rented: bool = False
    
    def rent(self) -> None:
        '''Contrassegna il film come noleggiato se non è già noleggiato.\nSe il film
        non è già noleggiato imposta is_rented a True, altrimenti stampa il messaggio "Il
        film '{self.title}' è già noleggiato."'''
        if self.is_rented:
            print(f"Il film '{self.title}' è già noleggiato.")
        else:
            self.is_rented = True
    
    def return_movie(self) -> None:
        '''Contrassegna il film come restituito.\nSe il film è già noleggiato
        imposta is_rented a False, altrimenti stampa il messaggio "Il film '{self.title}' non è
        stato noleggiato da questo cliente."'''
        if not self.is_rented:
            print(f"Il film '{self.title}' non è stato noleggiato da questo cliente.")
        else:
            self.is_rented = False
    
    def __str__(self):
        return f"{self.title}"
        
class Customer:
    _ids: list[str] = []

    def __init__(self, customer_id: str, name: str) -> None:
        if customer_id in Customer._ids:
            raise ValueError(f"Esiste già un cliente con id \"{customer_id}\"")
        self.customer_id = customer_id
        Customer._ids.append(customer_id)

        self.name = name
        self.rented_movie: list[Movie] = []

    def rent_movie(self, movie: Movie) -> None:
        '''Rimuove il film dalla lista rented_movies se già
        presente, altrimenti stampa il messaggio "Il film '{movie.title}' non è stato
        noleggiato da questo cliente."'''
        if not movie.is_rented:
            self.rented_movie.append(movie)
        movie.rent()
    
    def return_movie(self, movie: Movie) -> None:
        '''Contrassegna il film come restituito.\nSe il film è già noleggiato
        imposta is_rented a False, altrimenti stampa il messaggio "Il film '{self.name}' non è
        stato noleggiato da questo cliente."'''
        if  movie in self.rented_movie:
            self.rented_movie.remove(movie)
        movie.return_movie()

class VideoRentalStore:
    def __init__(self):
        self.movies: dict[str, Movie] = {}
        self.customers: dict[str, Customer] = {}
    
    def add_movie(self, movie_id: str, title: str, director: str) -> None:
        '''Aggiunge un nuovo film nel
        videonoleggio se non è già presente, altrimenti st  ampa il messaggio "Il film con
        ID '{movie_id}' esiste già."'''
        if movie_id in self.movies:
            print(f"Il film con ID '{movie_id}' esiste già.")
        else:
            movie: Movie = Movie(movie_id=movie_id, title=title, director=director)
            self.movies[movie_id] = movie
    
    def register_customer(self, customer_id: str, name: str) -> None:
        '''Iscrive un nuovo cliente nel
        videonoleggio se non è già presente, altrimenti stampa il messaggio "Il cliente
        con ID '{customer_id}' è già registrato."'''
        if customer_id in self.customers:
            print(f"Il film con ID '{customer_id}' esiste già.")
        else:
            customer: Customer = Customer(customer_id=customer_id, name=name)
            self.customers[customer_id] = customer
    
    def rent_movie(self, customer_id: str, movie_id: str) -> None:
        '''Permette al cliente di noleggiare un
        film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
        "Cliente o film non trovato."'''
        if customer_id in self.customers and movie_id in self.movies:
            self.customers[customer_id].rent_movie(self.movies[movie_id])
        else:
            print("Cliente o film non trovato.")
    
    def return_movie(self, customer_id: str, movie_id: str) -> None:
        '''Permette al cliente di restituire un
        film se entrambi esistono nel videonoleggio, altrimenti stampa il messaggio
        "Cliente o film non trovato."'''
        if customer_id in self.customers and movie_id in self.movies:
            self.customers[customer_id].return_movie(self.movies[movie_id])
        else:
            print("Cliente o film non trovato.")
    
    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        '''Restituisce la lista dei film
        noleggiati dal client (customer.rented_movies) se il cliente esiste nel
        videonoleggio, altrimenti stampa il messaggio "Cliente non trovato." e ritorna una
        lista vuota'''
        if customer_id in self.customers:
            return self.customers[customer_id].rented_movie
        else:
            print("Cliente non trovato.")
            return []
    
    def all_rented_movies(self) -> list[Movie]:
        '''Ritorna la lista di tutti i film che sono correntemente affittati da tutti gli utenti'''
        res = []
        for customer in self.customers.values():
            res.extend(customer.rented_movie)
        return res