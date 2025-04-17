from biblioteca import Biblioteca
from libro import Libro

biblio1: Biblioteca = Biblioteca()
div_comm: Libro = Libro("Divina Commedia", "Dante")
prom_sposi: Libro = Libro("I promessi sposi", "Alessandro Manzoni")
libro1: Libro = Libro("titolo generico", "autore generico")
print(biblio1.aggiungi_libro(div_comm))  # il libro "Divina Commedia" è stato aggiunto alla biblioteca.
print(biblio1.aggiungi_libro(libro1))  # il libro "titolo generico" è stato aggiunto alla biblioteca.
print(biblio1.aggiungi_libro(prom_sposi))  # il libro "I promessi sposi" è stato aggiunto alla biblioteca.

print("\n", biblio1.mostra_libri_disponibili(), sep="")  # ['Divina Commedia', 'titolo generico', 'I promessi sposi']

print(biblio1.presta_libro("Questo libro non esiste"))  # Il libro che stavi cercando non è in questa biblioteca.
print(biblio1.presta_libro("Divina Commedia"))  # Libro "Divina Commedia" prestato con successo!
print(biblio1.presta_libro("Divina Commedia"))  # Il libro "Divina Commedia" è già stato prestato.
print(biblio1.presta_libro("I promessi sposi"))  # Libro "I Promessi Sposi" prestato con successo!

print("\n", biblio1.mostra_libri_disponibili(), sep="")  # ['titolo generico']

print(biblio1.presta_libro("tiTOLO gEnEriCO")) # Libro "Titolo Generico" prestato con successo!

print("\n", biblio1.mostra_libri_disponibili(), sep="")  # Nessun libro disponibile al momento!

print("\n", biblio1.restituisci_libro("Questo libro non esiste"), sep="")  # Il libro che vuoi restituire non appartiene a questa biblioteca.
print(biblio1.restituisci_libro("Divina Commedia"))  # Libro "Divina Commedia" restituito con successo!
print(biblio1.restituisci_libro("Divina Commedia"))  # Il libro "Divina Commedia" non è in stato di prestito.
print(biblio1.restituisci_libro("I promessi sposi"))  # Libro "I Promessi Sposi" restituito con successo!
print(biblio1.restituisci_libro("tiTOLO gEnEriCO"))  # Libro "Titolo Generico" restituito con successo!

print("\n", biblio1.mostra_libri_disponibili(), sep="")  # ['Divina Commedia', 'titolo generico', 'I promessi sposi']
