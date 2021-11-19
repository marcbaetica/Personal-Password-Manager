import sqlite3


conn = sqlite3.connect('credentials.db')

cursor = conn.cursor()

# cursor.execute("""CREATE TABLE credentials(
#                     site TEXT,
#                     user TEXT,
#                     password TEXT
#                 )""")

# cursor.execute("INSERT INTO credentials VALUES ('some_site', 'user1', 'some_pass')")

# cursor.execute("SELECT * FROM credentials")
# cursor.execute("SELECT * FROM credentials WHERE site='some_site'")
# cursor.execute("SELECT * FROM credentials WHERE site='some_siteaa'")

# print(cursor.fetchall())
# fetchone() (returns None if no more rows available) and fetchmany(5) (returns max items as list)

# returns an iterable of type <class 'sqlite3.Cursor'>

data = cursor.execute("SELECT * FROM credentials WHERE site='some_site'")
print(type(data))
print([item for item in data])

conn.commit()

