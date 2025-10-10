from typing import Any

def foo(num: int) -> int:
    return num ** 2

# C'è una differenza tra referenziare una funzione e chiamarla
print(foo(2)) # Questo è chiamare una funzione. Usa le () e significa eseguire il codice all'interno della funzione

print(foo) # Questo è referenziare una funzione. Significa indicare la zona di memoria dove si trova la funzione