from libro import Libro

class Biblioteca:
    def __init__(self):
        self.lista_libri: list[Libro] = []
    
    def aggiungi_libro(self, libro: Libro) -> str:
        self.lista_libri.append(libro)
        return f"il libro \"{libro.titolo}\" è stato aggiunto alla biblioteca."
    
    def presta_libro(self, titolo: str) -> str:
        for libro in self.lista_libri:
            if libro.titolo.lower() == titolo.lower():
                if not libro.prestato:
                    libro.prestato = True
                    return f"Libro \"{titolo.title()}\" prestato con successo!"
                else:
                    return f"Il libro \"{titolo.title()}\" è già stato prestato."
        return "Il libro che stavi cercando non è in questa biblioteca."
    
    def restituisci_libro(self, titolo: str) -> str:
        for libro in self.lista_libri:
            if libro.titolo.lower() == titolo.lower():
                if libro.prestato:
                    libro.prestato = False
                    return f"Libro \"{titolo.title()}\" restituito con successo!"
                else:
                    return f"Il libro \"{titolo.title()}\" non è in stato di prestito."
        return "Il libro che vuoi restituire non appartiene a questa biblioteca."
    
    def mostra_libri_disponibili(self) -> list[str]:
        libri_disp: list[str] = [lib.titolo for lib in self.lista_libri if not lib.prestato]
        if libri_disp:
            return libri_disp
        else:
            return "Nessun libro disponibile al momento!"