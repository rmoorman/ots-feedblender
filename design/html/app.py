from flask import Flask
from flask import url_for, render_template, Response


app = Flask(__name__)


@app.route("/")
def index():
    pages = [
        url_for("add"),
        url_for("edit"),
        url_for("list"),
    ]
    return render_template("index.html", pages=pages)

@app.route("/add/")
def add():
    return render_template("add.html")

@app.route("/edit/")
def edit():
    return render_template("edit.html")

@app.route("/list/")
def list():
    return render_template("list.html")

@app.route("/feed.xml")
def feed():
    xml = render_template("feed.xml")
    return Response(xml, mimetype="application/xml")
