import sqlite3
import sys

cnct = sqlite3.connect('prototype.db')
sqc = cnct.cursor()


def init():
  sqc.execute("""CREATE TABLE IF NOT EXISTS accounts
              (id text, name text, status text)""")
  sqc.execute("delete from accounts")
  sqc.execute("""
    INSERT INTO accounts VALUES 
    ('AE_01235','Amuro','ENABLE'),
    ('AE_01236','Bright','ENABLE'),
    ('AE_01237','Char','ENABLE'),
    ('AE_01238','Dozle','DISABLE'),
    ('AE_01239','Emma','DISABLE'),
    ('AE_01240','Fraw','ENABLE')""")

  cnct.commit()

  cnct.close()


def check():
  sqc.execute("SELECT * FROM accounts")
  print(sqc.fetchall())
  cnct.close()


if __name__ in "__main__":
  if '-l' in sys.argv:
    check()
  else:
    init()