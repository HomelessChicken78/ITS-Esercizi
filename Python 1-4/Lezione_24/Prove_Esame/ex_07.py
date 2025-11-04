'''Scrivi una funzione che verifica se una combinazione di condizioni (A, B, e C) è soddisfatta per procedere con un'operazione.
L'operazione può procedere solo se la condizione A è vera o se entrambe le condizioni B e C sono vere.
La funzione deve ritornare "Operazione permessa" oppure "Operazione negata" a seconda delle condizioni che sono soddisfatte.'''

def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    return "Operazione permessa" if conditionA or (conditionB and conditionC) else "Operazione negata"