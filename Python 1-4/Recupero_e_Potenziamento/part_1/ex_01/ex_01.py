'''
Esercizio 1.

Un garage fa pagare una tariffa minima di 2.00 $ per parcheggiare fino a tre ore, più 0.50 $ all'ora per ogni ora o parte
di essa oltre le tre ore. Il costo massimo per un dato periodo di 24 ore di parcheggio ammonta a 10.00 $. Supponete
che nessuna macchina resti parcheggiata per più di 24 ore.
Elaborare un algoritmo che calcoli e stampi i costi del parcheggio per una data periodo di tempo.

Una volta elaborato l'algoritmo, scrivere in Python, una funzione calculateCharges che consenta di determinare il
costo del parcheggio per un dato cliente.
 
Scrivere un codice Python che consenta di calcolare i costi del parcheggio per ciascuno dei tre clienti che ieri hanno
parcheggiato le loro auto in questo garage.
Mostra, poi, i risultati in forma tabellare.
Il vostro output deve avere il seguente formato:

Car         Hours           Charge
 1                1.5            2.00 $
 2                4.0            2.50 $
 3              24.0           10.00 $
 TOTAL      29.5           14.50 $  
 '''

def park_cost(hrs: float) -> float:
    cost: float = 10

    if hrs < 24:
        if hrs >= 3:
            cost = 0.5*(hrs-3) + 2
        else:
            cost = 2
        
    return cost

car1: float = park_cost(1.5)
car2: float = park_cost(4)
car3: float = park_cost(24)

print(f"{'Car':<10}{'Hours':<10}Charge")
print(f"{'1':<10}{1.5:<10}{car1}")
print(f"{'2':<10}{4:<10}{car2}")
print(f"{'3':<10}{24:<10}{car3}")
print(f"{'TOTAL':<10}{29.5:<10}{car1+car2+car3}")