from flask import redirect, render_template, request, session
from flask_app import app, update_model
from flask_app.models import Mood, Rating
from flask_app.config.psqlconnect import connectToPSQL
import pandas as pd
import json
import plotly
from plotly.subplots import make_subplots
import plotly.express as px

@app.route("/")
def index():
  query =  """
  SELECT ratings.red as red, ratings.green as green, ratings.blue as blue, moods.name as mood
  FROM ratings JOIN moods ON ratings.mood_id = moods.id
  ORDER BY ratings.id DESC LIMIT 100;
  """
  df = pd.DataFrame(connectToPSQL().query_db(query),columns=["Red","Green","Blue","Mood"])
  fig = px.scatter_3d(df,x="Red",y="Green",z="Blue",color="Mood",
                range_x=[0,255],range_y=[0,255],range_z=[0,255],
                title="RGB Values by User Rated Moods")
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return render_template("index.html",graph = graphJSON)

@app.route("/train", methods=["GET","POST"])
def training():
  if request.method == "GET":
    if "user" in session:
      return render_template("train.html", moods=Mood.get_all())
    return redirect("/register")
  data = {**request.form, "user":session['user']}
  print(data)
  if Rating.validate(data):
    Rating.save(data)
    return "True"
  return "False"

@app.route("/test")
@app.route("/users/<int:id>")
@app.route("/about")
def coming_soon(id=0):
  return render_template("coming_soon.html")
