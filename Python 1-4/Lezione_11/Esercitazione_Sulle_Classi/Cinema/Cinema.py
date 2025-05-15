class Film:
    def __init__(self, titolo: str, durata_minuti: int):
        self._titolo = titolo
        self._durata_minuti = durata_minuti
    
    def get_titolo(self) -> str:
        return self._titolo
    
    def get_durata(self) -> int:
        return self._durata_minuti
    
class Sala:
    def __init__(self, id: str, posti_tot: int, posti_prenotati: int, Film: Film = None):
        self._id = id
        self._posti_tot = posti_tot
        self._posti_prenotati = posti_prenotati
        self._Film = Film
    
    def _get_id(self) -> str:
        return self._id
    
    def posti_disponibili(self) -> int:
        return self._posti_tot - self._posti_prenotati
    
    def prenota_posti(self, numero: int) -> str:
        p = "posto" if numero == 1 else "posti"
        if numero < 0:
            raise ValueError(f"\n{numero}\n^^^\nNon è possibile prenotare un numero di posti negativo")
        if self.posti_disponibili() >= numero:
            self._posti_prenotati += numero
            return f"{numero} {p} prenotati correttamente"
        else:
            return f"Non è stato possibile prenotare {numero} {p}"
        
    def change_film(self, film: Film) -> None:
        self._Film = film
    
class Cinema:
    __lista_sale: list[Sala] = []

    def __init__(self):
        self.sale = []
    
    def aggiungi_sala(self, sala: Sala) -> None:
        if sala in Cinema.__lista_sale:
            raise ValueError(f"La sala {sala._get_id()} si trova già in un'altro cinema")
        
        elif not isinstance(sala, Sala):
            raise ValueError("Perfavorre inserire una sala")

        for s in self.sale:
            if s._get_id() == sala._get_id():
                raise ValueError("Non possono esistere due sale con lo stesso id nello stesso cinema")

        Cinema.__lista_sale.append(sala)
        self.sale.append(sala)

    def get_sale(self) -> list[Sala]:
        return [s._get_id() for s in self.sale]
    
    def prenota_film(self, titolo: str, numero: int) -> str:
        p = "posto" if numero == 1 else "posti"
        for s in self.sale:
            if s._Film.get_titolo().lower() == titolo.lower() and s.prenota_posti(numero) == f"{numero} {p} prenotati correttamente":
                return f"Film {titolo.title()} trovato correttamente e prenotati {numero} {p}"
        return f"Non è stato possibile trovare alcun film con il titolo \"{titolo.title()}\" o nessuna delle sale ha {numero} {p} disponibili"