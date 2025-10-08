'''🔹 Esercizi su url_for()

    1. Generazione link interni

        Usare url_for per creare automaticamente i link alle route definite, ed esporli in una pagina principale (homepage con link a /about, /user/..., ecc.).

    2. Navigazione dinamica

        Creare una pagina con elenco utenti fittizi e i relativi link ai loro profili generati con url_for.

    3. Mini blog

        Definire route /post/<int:id> che restituisca un articolo fittizio.

        Creare una pagine /posts con un elenco di post e i relativi link agli articoli generati tramite url_for.
'''

from flask import Flask, url_for

app = Flask(__name__)
@app.route("/")
def home() -> str:
    return "<h1>Benvenuto!</h1><br />" \
    f"<h3><a href=\"{url_for('show_about')}\">/about</a><br />" \
    f"<a href=\"{url_for('person', nome='Cristiano')}\">/user</a><br />" \
    f"<a href=\"{url_for('list_persons')}\">/users</a><br />" \
    f"<a href=\"{url_for('list_posts')}\">/posts</a><br />" \
    "</h3>"

@app.route("/user/<nome>")
def person(nome: str) -> str:
    return f"<h1>Benvenuto, {nome}!</h1>"

@app.route("/about")
def show_about() -> str:
    return "<h2>Questa è una app fatta con Flask.</h2>"

@app.route("/square/<int:n>")
def power(n: int) -> str:
    return f"<h3>{n*n}</h3>"

@app.route("/sum/<int:a>/<int:b>")
def sum(a: int, b: int) -> str:
    return f"<h3>{a+b}</h3>"

@app.route("/users")
def list_persons() -> str:
    persons: list[str] = ["Nicol", "Cristiano", "Alfredo", "Paolo"]

    res: str = "<h3>"

    for p in persons:
        res += f"<a href=\"{url_for('person', nome=p)}\">{p}</a><br />"
    
    return res + "</h3>"

@app.route("/post/<int:id>")
def post(id) -> str:
    return f"<h3>Post {id}</h3>"

@app.route("/posts")
def list_posts() -> str:
    posts: list[int] = [4, 50, 221, 374, 24, 0, 37, 5, 457]

    res: str = "<h3>"
    for p in posts:
        res += f"<a href=\"{url_for('post', id=p)}\">{p}</a><br />"

    return res + "</h3>"