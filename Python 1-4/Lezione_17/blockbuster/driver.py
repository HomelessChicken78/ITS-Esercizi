'''### Test con codice driver
Scrivere un codice driver in cui si crea una lista di 10 film, di cui 5 sono film d'azione, 4 sono commedie e 1 è un film drammatico.

Successivamente:

    Creare un oggetto Noleggio.
    Stampare:     
    
    
'''

from movie_genre import *
from noleggio import *

# 5 Film d'azione
a1: Azione = Azione(0, "Azione 1")
a2: Azione = Azione(1, "Azione 2")
a3: Azione = Azione(2, "Azione 3")
a4: Azione = Azione(3, "Azione 4")
a5: Azione = Azione(4, "Azione 5")

# 4 Commedie
c1: Commedia = Commedia(5, "Commedia 1")
c2: Commedia = Commedia(6, "Commedia 2")
c3: Commedia = Commedia(7, "Commedia 3")
c4: Commedia = Commedia(8, "Commedia 4")

# 1 Film drammatico
d1: Drama = Drama(9, "Drammatico 1")

noleggio: Noleggio = Noleggio([a1, a2, a3, a4, a5, c1, c2, c3, c4, d1])

# Simulare il noleggio di un film di un primo cliente.
print("Quale film vuoi noleggiare?")
noleggio.rentAMovie(a1, 0)

# Simulare il noleggio di un secondo film sempre da parte del primo cliente.
print()
noleggio.rentAMovie(c3, 0)

# Simulare il noleggio del film precedente da parte di un secondo cliente.
# (assicurarsi che il codice avvisi il secondo cliente che il film richiesto non è disponibile).
print()
noleggio.rentAMovie(c3, 1)

# Simulare il noleggio di un terzo film da parte del secondo cliente.
print()
noleggio.rentAMovie(c2, 1)

# Simulare il reso del secondo film noleggiato dal primo cliente.
print()
noleggio.giveBack(c3, 0, 3)

# Stampare la lista dei film disponibili in negozio.
print("\nLista di Film disponibili:")
noleggio.printMovies()