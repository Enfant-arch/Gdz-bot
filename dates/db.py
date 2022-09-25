import asyncio
import psycopg2
import logging
conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                        password="root",
                        port="5432")
conn.autocommit = True
cursor = conn.cursor()
###UNCOMMIT WHEN INSTALL ON VM
'''
cursor = conn.cursor()
cursor.execute("""CREATE TABLE users (user_id BIGINT PRIMARY KEY , user_name VARCHAR(50), user_act bool)""" )
cursor.execute("SELECT version();")
conn.commit()
print(cursor.fetchall())
'''


class db:
  def __init__(self, name, id, activity):
    self.name = name
    self.id = id
    self.activity = activity
    self.cou = 0

  async def add(self):
    try:
      cursor.execute(f"INSERT INTO users (user_id, user_name, user_act) VALUES ({self.id}, '{self.name}', {self.activity})")
    except Exception as err:
      self.cou += 1

  async def up_activaty(self):
    cursor.execute(f"SELECT * FROM users WHERE id={self.id}")
    cursor.executemany("INSERT INTO user activity=?", True)  

  async def down_activaty(self):
    cursor.execute(f"SELECT * FROM users WHERE id={self.id}")
    cursor.executemany("INSERT INTO user activity=?", False)

  async def send_all_count(self):
    cursor.execute("SELECT COUNT(user_id) FROM users;")
    return str(cursor.fetchall()[0]).replace(",", "")
  
  def enject_user_id():
    cursor.execute("SELECT user_id FROM users;")
    return cursor.fetchall()

  def send_user_id():
    bad_practice = db.enject_user_id()
    print(bad_practice)
    nice_practice = []
    for i in bad_practice:
      j = str(i)
      nice_practice.append(j[1: -1])
      print(j[1: -2])
    return nice_practice

 