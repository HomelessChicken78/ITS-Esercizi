'''
1) Scrivi una funzione che verifica se una combinazione di condizioni (X, Y, e Z) è
soddisfatta per procedere con un'azione. L'azione può procedere solo se la condizione X
è vera e almeno una tra Y e Z è vera. La funzione deve ritornare "Azione permessa"
oppure "Azione negata" a seconda delle condizioni che sono soddisfa

True, True, True -> "Azione permessa"
True, False, True -> "Azione permessa"
True, True, False -> "Azione permessa"
False, True, True -> "Azione negata"
True, False, False -> "Azione negata"
'''

def special_condition(X: bool, Y: bool, Z: bool) -> str:
    return "Azione permessa" if X and (Y or Z) else "Azione negata"

if __name__ == "__main__":
    print(special_condition(True, True, True))
    print(special_condition(True, False, True))
    print(special_condition(True, True, False))
    print(special_condition(False, True, True))
    print(special_condition(True, False, False))