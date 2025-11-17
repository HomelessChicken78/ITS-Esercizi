'''🔹 Esercizi su routing statico e dinamico

    1. Route dinamica per profilo utente

        Creare un percorso /user/<nome> che restituisca “Benvenuto, <nome>!”.

        Testare con nomi diversi nell’URL.

    2. Route con parametri numerici

        Definire /square/<int:n> che ritorni il quadrato di n.

    3. Parametri multipli

        Creare /sum/<int:a>/<int:b> che restituisca la somma dei due numeri.
'''

from flask import Flask

app = Flask(__name__)
@app.route("/")
def home() -> str:
    return "<h1>Benvenuto!</h1>"

@app.route("/user/<string:nome>")
def person(nome: str) -> str:
    return f"<h1>Benvenuto, {nome}!</h1>"

@app.route("/square/<int:n>")
def power(n: int) -> str:
    return f"<h3>{n*n}</h3>"

@app.route("/sum/<int:a>/<int:b>")
def sum(a: int, b: int) -> str:
    return f"<h3>{a+b}</h3>"