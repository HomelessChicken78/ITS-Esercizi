from re import search

class Documento:
    _testo: str

    def __init__(self, testo):
        self.setText(testo)

    def setText(self, testo: str) -> None:
        self._testo = testo
    
    def  getText(self) -> str:
        return self._testo
    
    def isInText(self, chiave: str) -> bool:
        '''Restituisce True se un documento contiene la parola
        chiave specificata.'''
        if search(chiave, self.getText()):
            return True
        return False
    
class Email(Documento):
    _mittente: str
    _destinatario: str
    _titolo_messaggio: str
    def __init__(self, testo: str, mittente: str, destinatario: str, titolo_messaggio: str):
        super().__init__(testo)
        self.setMittente(mittente)
        self.setDestinatario(destinatario)
        self.setTitoloMessaggio(titolo_messaggio)
    
    def setMittente(self, mittente: str) -> str:
        self._mittente = mittente
    
    def setDestinatario(self, destinatario: str) -> str:
        self._destinatario = destinatario

    def setTitoloMessaggio(self, titolo_messaggio: str) -> str:
        self._titolo_messaggio = titolo_messaggio
    
    def getMittente(self) -> str:
        return self._mittente

    def getDestinatario(self) -> str:
        return self._destinatario

    def getTitoloMessaggio(self) -> str:
        return self._titolo_messaggio
    
    def getText(self) -> str:
        return f"Da: {self.getMittente()}, A: {self.getDestinatario()}\nTitolo: {self.getTitoloMessaggio()}\nMessaggio: {self._testo}"
    
    def writeToFile(self, path) -> None:
        with open(path, "w") as file:
            file.write(self.getText())

class File(Documento):
    _nomePercorso: str

    def __init__(self, nomePercorso):
        self._nomePercorso = nomePercorso
        self.leggiTestoDaFile()
    
    def nomePercorso(self) -> str:
        return self._nomePercorso

    def leggiTestoDaFile(self) -> None:
        with open(self.nomePercorso(), "r") as f:
            self.setText(f.read())
    
    def getText(self) -> str:
        return f"Percorso: {self.nomePercorso()}\nContenuto: {self._testo}"