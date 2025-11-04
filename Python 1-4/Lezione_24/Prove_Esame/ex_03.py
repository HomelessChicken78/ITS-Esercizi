'''Scrivi una funzione che accetti un dizionario di prodotti con i prezzi
e restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo
superiore a 20, ma scontati del 10%.'''

def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    res: dict[str:float] = dict()

    for prod, cost in prodotti.items():
        if cost >= 20:
            res[prod] = cost - (cost * 0.1)
    
    return res