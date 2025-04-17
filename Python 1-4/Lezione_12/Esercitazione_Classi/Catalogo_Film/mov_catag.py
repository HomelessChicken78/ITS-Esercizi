class MovieCatalog:
    def __init__(self):
        self.__catalog: dict[str:list[str]] = {}

    def add_movie(self, director_name: str, movies: list[str]) -> None: 
        '''Aggiunge uno o più film a un regista specifico nel catalogo.\n
        Se il regista non esiste, viene creato un nuovo record.\n
        Se il regista esiste, la sua lista di film viene aggiornata.'''
        director_name = director_name.lower()
        movies = [m.lower() for m in movies]
        if director_name not in self.__catalog.keys():
            self.__catalog[director_name] = []
        self.__catalog[director_name] += movies

    def remove_movie(self, director_name: str, movie_name: str) -> None: 
        '''Rimuove un film specifico dall'elenco dei film di un regista.\n
        Se tutti i film sono rimossi, il regista può essere opzionalmente rimosso dal catalogo.'''
        director_name = director_name.lower()
        movie_name = movie_name.lower()
        if director_name in self.__catalog.keys():
            if movie_name in self.__catalog[director_name]:
                self.__catalog[director_name].remove(movie_name)
                if not self.__catalog[director_name]:
                    self.__catalog.pop(director_name)
            else:
                print(f"The movie you are searching for either doesn't exist or is not directed by {director_name}.")
        else:
            print("The director you are searching for is not in the catalog.")


    def list_directors(self) -> None:
        '''Elenca tutti i registi presenti nel catalogo.'''
        print('\n'.join(self.__catalog.keys()))

    def get_movies_by_director(self, director_name: str) -> list[str]:
        '''Restituisce tutti i film di un regista specifico.'''
        director_name = director_name.lower()
        if director_name in self.__catalog:
            return self.__catalog[director_name]
        return "No director with that name could be found."

    def search_movies_by_title(self, title: str) -> list[str]:
        '''Trova tutti i film che contengono una certa parola nel titolo. Restituisce un elenco
        dei registi e dei rispettivi film che contengono la parola cercata o un messaggio di errore se nessun film contiene la
        parola cercata nel titolo.'''
        title = title.lower()
        # Create a list with all of the movies, without indicating the directors.
        movies: list[str] = []
        for li in self.__catalog.values():
            for m in li:
                movies.append(m)
        
        # Create a list which contain all the succesful matches
        result = [m for m in movies if title in m]

        # If the result is empty return an error.
        if result:
            return result
        else:
            return "No match could be found."


