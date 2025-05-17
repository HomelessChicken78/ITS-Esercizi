class Indirizzo:
    def __init__(self, via: str, civico: str, cap: str):
        self.via = via
        self.civico = civico
        self.cap = cap

    def __repr__(self) -> str:
        return f"Indirizzo(\"{self.via}\", \"{self.civico}\", \"{self.cap}\")"
    
    def get_via(self) -> str:
        return self.via
    
    def get_civico(self) -> str:
        return self.civico
    
    def get_cap(self) -> str:
        return self.cap
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Indirizzo) or hash(self) != hash(other):
            return False
        return (self.get_via(), self.get_civico(), self.get_cap()) == (other.get_via(), other.get_civico(), other.get_cap())
    
    def __hash__(self):
        return hash((self.get_via(), self.get_civico(), self.get_cap()))

if __name__ == "__main__":
    a: Indirizzo = Indirizzo("Via di casa mia", "400bis", "00054")
    b: Indirizzo = Indirizzo("via dei guanti", "15", "1017")
    c: Indirizzo = Indirizzo("Via di casa mia", "400bis", "00054")
    print(a is c)
    print(a == c)
    print(a == b)
    print(a == "c")

    fiu: list[Indirizzo] = [a, b, c]
    for indirizzo in fiu:
        print(indirizzo)

    if a in fiu:
        print(a, "esiste nella città fiu")

    if Indirizzo("Via di casa mia", "400bis", "00054") in fiu:
        print("certo")