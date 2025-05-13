class Indirizzo:
    def __init__(self, via: str, civico: int):
        self._via = via
        self._civico = civico
    
    def getVia(self) -> str:
        return self._via
    
    def getCivico(self) -> int:
        return self._civico
    
    def __repr__(self):
        return f"Indirizzo(\"{self._via}, {self._civico}\")"
    
    def __eq__(self, other):
        if not isinstance(other, Indirizzo) or hash(self) != hash(other):
            return False
        return (self.getVia(), self.getCivico()) == (other.getVia(), other.getCivico())
    
    def __hash__(self):
        return hash((self.getVia(), self.getCivico()))

v1 = Indirizzo("Casa Mia", 4)
v2 = Indirizzo("Casa Mia", 4)
print(v1 == v2)
print(v1 == "Casa Mia, 4")
# print(hash(v1))
# print(hash(v2))

vie: list[Indirizzo] = [v1, v2, Indirizzo("ITS", 23), Indirizzo("Ciao", 42)]
for v in vie:
    print(v)