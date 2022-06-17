from flask_app import bcrypt
from flask_app.config.psqlconnect import connectToPSQL
from flask_app.config.regex import EMAIL_REGEX

class User:
  def __init__(self,data):
    self.id=data[0]
    self.username=data[1]
    self.email=data[2]
    self.password=data[3]

  def validate_pw(self,pw):
    return bcrypt.check_password_hash(self.password,pw)

  @classmethod
  def get_by_email(cls,data):
    data = {**data, "email": data["email"].lower()}
    query = 'SELECT * FROM users WHERE email=%(email)s;'
    results = connectToPSQL().query_db(query,data)
    return cls(results[0]) if len(results) > 0 else None

  @classmethod
  def get_by_id(cls,data):
    query = 'SELECT * FROM users WHERE id=%(id)s;'
    results = connectToPSQL().query_db(query,data)
    return cls(results[0]) if len(results) > 0 else None

  @classmethod
  def get_by_username(cls,data):
    query = 'SELECT * FROM users WHERE username=%(username)s;'
    results = connectToPSQL().query_db(query,data)
    return cls(results[0]) if len(results) > 0 else None

  @staticmethod
  def valid_reg(data):
    if len(data['username']) not in range(3,46):
      return False
    if(User.get_by_username(data)):
      return False
    if not EMAIL_REGEX.match(data['email']):
      return False
    if len(data['email']) > 100:
      return False
    if(User.get_by_email(data)):
      return False
    if len(data['password']) < 8:
      return False
    pw=data['password']
    if not pw == data['confirm_password']:
        return False
    return True

  @staticmethod
  def encrypt_password(data):
      hash=bcrypt.generate_password_hash(data['password'].encode('utf8'))
      newData={
          'email':data['email'].lower(),
          'username':data['username'],
          'password':hash.decode('utf8')
      }
      return newData

  @classmethod
  def save(cls,data):
    query="INSERT INTO users(email, username, password) VALUES(%(email)s, %(username)s, %(password)s) RETURNING id;"
    return connectToPSQL().query_db(query,User.encrypt_password(data))