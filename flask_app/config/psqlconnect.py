import os
import psycopg2

class PostgresConnection:
  def __init__(self):
    conn = psycopg2.connect(
      host="localhost",
      database="ML_with_flask",
      user=os.environ['DB_USERNAME'],
      password=os.environ['DB_PASSWORD'])
    self.connection = conn
  def query_db(self, query, data=None, verbose = False):
    with self.connection.cursor() as cursor:
      try:
        query = cursor.mogrify(query,data)
        if verbose:
          print(f"Running Query: {query}")
        executable = cursor.execute(query,data)
        if str(query).lower().find("insert") >= 0:
          self.connection.commit()
          return cursor.lastrowid
        elif str(query).lower().find("select") >= 0:
          result = cursor.fetchall()
          return result
        else:
          self.connection.commit()
      except Exception as e:
        print(f"Something went wrong: {e}")
      finally:
        self.connection.close()

def connectToPSQL():
  return PostgresConnection()