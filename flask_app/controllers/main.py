from flask import redirect, render_template
from flask_app import app, update_model


@app.route("/")
def index():
  return render_template("index.html")

