# Grazie a quanto detto prima, una funzione può prendere come parametro un'altra funzione

from typing import Callable, Any

def funct_di_funct(funct: Callable) -> Any:
    print("Questa è la zona di memoria della funzione", funct)
    print("Eseguo la funzione...")
    funct()

def f1() -> int:
    print("Funzione eseguita!")
    return "Ho eseguito la funzione"

# funct_di_funct(f1()) # Questo non passa la funzione come parametro a funct_di_funct, ma passa il return della funzione come parametro a funct_di_funct
# Ciò vuol dire che funct_di_funct riceverà come parametro "Ho eseguito la funzione", non la locazione di memoria di f1
# funct_di_funct prova a eseguire una stringa, ma fallisce perchè le stringhe non possono esser chiamate

print()

funct_di_funct(f1)