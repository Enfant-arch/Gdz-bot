import sqlite3

con = sqlite3.connect("dates/users.db")
cur = con.cursor()


class db:
  def __init__(self, name, id, activity):
    self.name = name
    self.id = id
    self.activity = activity


  async def add(self):
    user_tl = [
      (f"{self.name}", self.id, self.activity)
    ]
    cur.executemany(f"INSERT INTO user VALUES (?, ?, ?)", user_tl)
   
  async def up_activaty(self):
    await cur.execute(f"SELECT * FROM users WHERE id={self.id}")
    await cur.executemany("INSERT INTO user activity=?", True)  

  async def down_activaty(self):
    await cur.execute(f"SELECT * FROM users WHERE id={self.id}")
    await cur.executemany("INSERT INTO user activity=?", False)

  async def exist(self):
    indet = cur.execute(f"SELECT user_id FROM user WHERE user_id='{self.id}';").fetchall()
    return indet
