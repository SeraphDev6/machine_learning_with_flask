import os
from urllib.parse import urlparse
import psycopg2

class PostgresConnection:
  def __init__(self):
    url = urlparse(os.environ.get('DATABASE_URL'))
    db = "dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname)
    conn = psycopg2.connect(db)
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
          return cursor.fetchone()[0]
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