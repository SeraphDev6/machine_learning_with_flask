import os
from flask import Flask
from joblib import dump, load
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key= os.environ['SECRET_KEY']

bcrypt = Bcrypt(app)
model = load("./model.joblib")

def update_model(new_model, model_name = "model"):
  global model
  dump(new_model,f"./{model_name}.joblib")
  model = load(f"./{model_name}.joblib")