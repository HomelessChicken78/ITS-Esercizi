from Magazzino import *

mela: Prodotto = Prodotto("Mela", 5)
# print(mela)
# print(mela.data())
olio: Prodotto = Prodotto("olio", 0)
farina: Prodotto = Prodotto("farina", 25)
pasta: Prodotto = Prodotto("pasta", 75)
biscotto: Prodotto = Prodotto("biscotti", 23)

m1: Magazzino = Magazzino()

# Prova ad aggiungere un nuovo prodotto:
m1.aggiungi_prodotto(mela)
print("Lista prodotti in m1:\n", m1.prodotti, "\nProvo ad aggiungere mela di nuovo...")
m1.aggiungi_prodotto(mela)
print("Lista prodotti in m1:\n", m1.prodotti)

m1.aggiungi_prodotto(olio)
m1.aggiungi_prodotto(farina)
m1.aggiungi_prodotto(pasta)
m1.aggiungi_prodotto(biscotto)

# Prova a cercare un prodotto
print("\n",m1.cerca_prodotto("farina"), sep="")
print("\n",m1.cerca_prodotto("olio"), sep="")

# Prova a verificare la disponibilità:
print("\n", m1.verifica_disponibilità("biscotti"))
print("\n", m1.verifica_disponibilità("olio"))
print("\n", m1.verifica_disponibilità("salsiccia"))