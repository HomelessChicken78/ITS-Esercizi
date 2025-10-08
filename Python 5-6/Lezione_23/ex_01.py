'''🔹 Esercizio di base

    Definire un route /about

        Definire una route /about che ritorni un breve testo HTML con descrizione dell’app o dell’autore.'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home() -> str:
    return "Welcome!"

@app.route("/about")
def show_about() -> str:
    return "<h2>Questa è una app fatta con Flask.</h2>"