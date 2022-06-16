from flask_app.config.psqlconnect import connectToPSQL


class Mood:
  def __init__(self,data):
    self.id = data[0]
    self.name = data[1]

  @classmethod
  def get_all(cls):
    query = 'SELECT * FROM moods;'
    results = connectToPSQL().query_db(query)
    return [cls(result) for result in results]

  @classmethod
  def get_by_id(cls,data):
    query = 'SELECT * FROM moods WHERE id = %(id)s;'
    results = connectToPSQL().query_db(query, data, True)
    return cls(results[0]) if len(results) > 0 else None