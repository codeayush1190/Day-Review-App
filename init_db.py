import os
import sqlite3

connection = sqlite3.connect("Python Advancing\\Flask\\database.db")

with open(os.path.join(os.getcwd(), "Python Advancing\\Flask\\schema.sql")) as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Project', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Project', 'Content for the second post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Third Project', 'Content for the second post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Forth Project', 'Content for the second post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Fifth Project', 'Content for the second post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Sixth Project', 'Content for the second post')
            )

connection.commit()
connection.close()