from flask import Flask
from flask import url_for, render_template, flash, Response
from BeautifulSoup import BeautifulSoup


app = Flask(__name__)
app.secret_key = "A962B60B-765C-49A1-AF45-7C061605B34F"


@app.after_request
def after_request(response):
    if response.mimetype == "text/html":
        response.data = BeautifulSoup(response.data).prettify()
    return response


@app.route("/")
def index():
    pages = [
        url_for("add"),
        url_for("added"),
        url_for("edit"),
        url_for("edited"),
        url_for("delete"),
        url_for("deleted"),
        url_for("list"),
    ]
    return render_template("index.html", pages=pages)

@app.route("/add/")
def add():
    return render_template("add.html")

@app.route("/list/added/")
def added():
    flash("the new blend has been added")
    return render_template("list.html", active_endpoint="list")

@app.route("/edit/")
def edit():
    return render_template("edit.html")

@app.route("/list/edited/")
def edited():
    flash("the blend data has been updated successfully")
    return render_template("list.html", active_endpoint="list")

@app.route("/delete/")
def delete():
    return render_template("delete.html")

@app.route("/list/deleted/")
def deleted():
    flash("the blend has been deleted")
    return render_template("list.html", active_endpoint="list")

@app.route("/list/")
def list():
    return render_template("list.html")

@app.route("/feed.xml")
def feed():
    xml = render_template("feed.xml")
    return Response(xml, mimetype="application/xml")
