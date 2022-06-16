from flask import redirect, render_template, request, session
from flask_app import app


@app.route("/register", methods=["GET","POST"])
def register():
  if request.method == "GET":
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")

@app.route("/logout")
def logout():
  session.clear()
  return redirect("/")