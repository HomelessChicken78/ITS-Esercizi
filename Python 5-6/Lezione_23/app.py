from flask import Flask, url_for

app = Flask(__name__) # Crea istanza di quella classe, che rappresenta la nostra app.
# app.run(port=4999)

@app.route('/')
def home() -> str:
    return "<h3>Hello World!</h3>"

@app.route('/end')
def end() -> str:
    return "<h3>Bye!</h3>"


@app.route('/user/<string:username>')
def show_user_profile(username: str) -> str:
    if username.lower() == "Nicol":
        return f"Profilo di {username}. È un noob"
    return f"Profilo di {username}"

@app.route('/post/<int:post_id>')
def show_post(post_id: str) -> str:
    return f"Post {post_id}"
# flask --app <nome_file> run
# Oppure se la app si chiama "app.py", flask run

with app.test_request_context():
    print(url_for('home'))
    print(url_for('show_user_profile', username='Rachele'))
    print(url_for('show_post', post_id=4))