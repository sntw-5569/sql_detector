import sqlite3

class DataBaseConnector():
  def __init__(self, *args, **kwargs):
    self.cnct = sqlite3.connect('prototype.db')
    self.sqc = self.cnct.cursor()

  def execute(self, sql):
    self.sqc.execute(sql)
    print("is not patched Mock.")
    return self.sqc.fetchall()

