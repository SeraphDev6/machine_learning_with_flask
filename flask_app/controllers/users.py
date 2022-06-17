from flask import redirect, render_template, request, session
from flask_app import app
from flask_app.models import User

@app.route("/register", methods=["GET","POST"])
def register():
  if request.method == "GET":
    if 'user' in session:
      return redirect('/')
    return render_template("register.html")
  if User.valid_reg(request.form):
    session['user']=User.save(request.form)
    return redirect("/")

@app.route("/login", methods=["GET","POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")

@app.route("/logout")
def logout():
  session.clear()
  return redirect("/")