'''
3) Scrivi una funzione che accetti un dizionario di prodotti con i relativi prezzi e
restituisca un nuovo dizionario con solo i prodotti che hanno un prezzo inferiore a 50, ma
con i prezzi aumentati del 10% e arrotondati a due cifre decimali.

{"mela" : 4.23334, "pera" : 5, "gioiello" : 230, "grano" : 1.01, "computer" : 1500} -> {"mela" : 4.66, "pera" : 5.50, "grano" : 1.11}
'''

def better_prices(prod: dict[str, float]) -> dict[str, float]:
    cheap_prod: dict[str, float] = {}

    for name, price in prod.items():
        if price < 50:
            cheap_prod[name] = float(round(price*1.1, 2))
    
    return cheap_prod

print(better_prices({"mela" : 4.23334, "pera" : 5, "gioiello" : 230, "grano" : 1.01, "computer" : 1500}))