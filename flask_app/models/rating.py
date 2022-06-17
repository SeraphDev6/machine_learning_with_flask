from flask_app.config.psqlconnect import connectToPSQL

class Rating:
  def __init__(self,data):
    self.id = data[0]
    self.red = data[1]
    self.green = data[2]
    self.blue = data[3]
    self.user = data[4]
    self.mood = data[5]

  @staticmethod
  def validate(data):
    for prop in ["red","green","blue","user"]:
      if prop not in data:
        return False
      if data["mood"] == "":
        return False
    return True
  
  @staticmethod
  def save(data):
    query = "INSERT INTO ratings(red, green, blue, user_id, mood_id) \
            VALUES(%(red)s, %(green)s, %(blue)s, %(user)s, %(mood)s);"
    return connectToPSQL().query_db(query,data)