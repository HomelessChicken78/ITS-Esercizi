from mov_catag import MovieCatalog

uci: MovieCatalog = MovieCatalog()


# Create directors and their movies
uci.add_movie("George Lucas", ["Star WaRs"])
uci.add_movie("Disney", ["The Lion King", "Snow White"])
uci.add_movie("disNEy", ["Pinocchio"])
uci.add_movie("George Lucas", ["Sole a catinelle"])
uci.add_movie("Checco Zalone", ["Quo vADo?", "cAdO dALLe NuBi"])
uci.add_movie("Me stesso", ["Film1", "Film2"])
#print(uci._MovieCatalog__catalog) # test "private" attribute

# Print the list of directors
print(uci.list_directors())

# Query director's film
print()
print(uci.get_movies_by_director("Federico March"))  # No director with that name could be found.
print(uci.get_movies_by_director("Checco Zalone"))  # ['Quo Vado?', 'Cado dalle Nubi']
print(uci.get_movies_by_director("George LuCAs"))   # ['Star Wars', 'Sole a catinelle']

# Remove movies from a director
print()
uci.remove_movie("Marco Cascio", "ITS: Il film")  # The director you are searching for is not in the catalog.
uci.remove_movie("George LuCAs", "Pinocchio")  # The movie you are searching for either doesn't exist or is not directed by George Lucas.
uci.remove_movie("George LuCAs", "SoLE a cATInelle")

print(uci.get_movies_by_director("geOrge LuCAS"))  # ['Star Wars']

# Test with removing a director if the list is empty
print("\nBefore removing \"me stesso\":")
print(uci.list_directors())
uci.remove_movie("me stesso", "Film1")
uci.remove_movie("me stesso", "Film2")
print("----------------\nAfter removing \"me stesso\":")
print(uci.list_directors())

# Testing search_movies_by_title
print()
print(uci.search_movies_by_title("Pino"))  #['Pinocchio']
print(uci.search_movies_by_title("a"))  #['star wars', 'quo vado?', 'cado dalle nubi']
print(uci.search_movies_by_title("I love the pizza"))  # No match could be found.

