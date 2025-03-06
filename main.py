import sqlite3
from flask import Flask
from flask import render_template, g

DATABASE = './storage/db.sqlite3'

app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('database/post.sql', mode='r') as f:
            db.executescript(f.read())
        db.commit()
init_db()

@app.route("/")
def home():
    return render_template("welcome.html")

@app.route("/blog")
def blog(posts=None):
    db = get_db()
    cursor = db.execute("SELECT * from posts")
    results = cursor.fetchall()
    print(len(results))
    return render_template("blog.html", posts=results)

