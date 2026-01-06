from flask import Flask, render_template
from models import Film, Memo
import json

app = Flask(__name__)

def load_films():
    with open("data/films.json") as f:
        return json.load(f)

@app.route("/")
def index():
    films = load_films()
    return render_template("index.html", films=films)

@app.route("/film/<title>")
def film_page(title):
    films = load_films()
    film = next(f for f in films if f["title"] == title)
    return render_template("film.html", film=film)
