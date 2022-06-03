import sqlite3

con = sqlite3.connect("users.db")
cur = con.cursor()

# cur.execute("SELECT * FROM USERS ORDER BY id DESC LIMIT 1")

cur.execute("SELECT * FROM USERS WHERE username='leotovell'")
print(cur.fetchall()[0])

