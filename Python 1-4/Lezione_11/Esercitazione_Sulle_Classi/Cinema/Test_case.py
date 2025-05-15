from Cinema import *

sala1: Sala = Sala("kjw85dah3", 20, 0)
film1: Film = Film("Paperino", 40)

# Prove con l'aggiunta di posti
print(sala1.posti_disponibili())
print(sala1.prenota_posti(20))
print(sala1.prenota_posti(1))
# print(sala1.prenota_posti(-20))
print(sala1.posti_disponibili())

sala1.change_film(film1)
print("Sala 1 al momento sta riproducendo", sala1._Film.get_titolo())

film2 = Film("Topolino e l'avventura", 90)
film3 = Film("Il mistero del castello", 120)

sala_bella: Sala = Sala("sala2", 30, 10)
sala_bella.change_film(film1)

sala2: Sala = Sala("sala2", 100, 10)
sala2.change_film(film2)

sala3: Sala = Sala("sala3", 30, 5)
sala3.change_film(film3)

sala4: Sala = Sala("sala4", 80, 0)
sala4.change_film(film1)

sala5: Sala = Sala("sala5", 25, 20)
sala5.change_film(film3)

sala6: Sala = Sala("sala6", 40, 10)
sala7: Sala = Sala("sala7", 60, 55)
sala8: Sala = Sala("sala8", 100, 0)
sala9: Sala = Sala("sala9", 75, 25)
sala10: Sala = Sala("sala10", 90, 60)
sala11: Sala = Sala("sala11", 50, 0)

uci1: Cinema = Cinema()
uci2: Cinema = Cinema()

uci1.aggiungi_sala(sala2)
uci1.aggiungi_sala(sala3)
uci1.aggiungi_sala(sala5)
print("\nSale in uci1:", uci1.get_sale())

# Prova ad aggiungere due sale con lo stesso id nello stesso cinema e poi in due cinema diversi
# uci1.aggiungi_sala(sala_bella)
uci2.aggiungi_sala(sala_bella)
print("Sale in uci2:", uci2.get_sale())

# Prova ad aggiungere una sala che si trova in un'altro cinema:
uci2.aggiungi_sala(sala4)
# uci1.aggiungi_sala(sala4)
# print([s._get_id() for s in Cinema._Cinema__lista_sale])

# Prova prenotazione film
print(uci1.prenota_film("Topolino e l'avventura", 89))
print(uci1.prenota_film("Topolino e l'avventura", 2))
print(uci1.prenota_film("Topolino e l'avventura", 1))

# Prova a prenotare un film che esiste in due sale diverse
print(f"\n\nPosti disponibili in sala3: {sala3.posti_disponibili()}")
print(f"Posti disponibili in sala5: {sala5.posti_disponibili()}")

print(uci1.prenota_film("Il mistero del castello", 29))
print(f"Posti disponibili in sala3: {sala3.posti_disponibili()}")
print(f"Posti disponibili in sala5: {sala5.posti_disponibili()}")

print(uci1.prenota_film("Il mistero del castello", 24))
print(f"Posti disponibili in sala3: {sala3.posti_disponibili()}")
print(f"Posti disponibili in sala5: {sala5.posti_disponibili()}")

print(uci1.prenota_film("Il mistero del castello", 5))
print(f"Posti disponibili in sala3: {sala3.posti_disponibili()}")
print(f"Posti disponibili in sala5: {sala5.posti_disponibili()}")

print(uci1.prenota_film("Il mistero del castello", 1))
print(f"Posti disponibili in sala3: {sala3.posti_disponibili()}")
print(f"Posti disponibili in sala5: {sala5.posti_disponibili()}")

print(uci1.prenota_film("Il mistero del castello", 1))