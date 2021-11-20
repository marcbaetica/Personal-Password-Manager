import sqlite3


conn = sqlite3.connect('credentials.db')

cursor = conn.cursor()


def create_db_and_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS credentials(
                        site TEXT,
                        user TEXT,
                        password TEXT
                    )""")


def insert_credential_into_table(site, user, password):
    cursor.execute(f"INSERT INTO credentials VALUES ('{site}', '{user}', '{password}'")
    conn.commit()


def return_all_credentials():
    cursor.execute("SELECT * FROM credentials")
    cursor.fetchall()


def return_credentials_for_site(site):
    cursor.execute(f"SELECT * FROM credentials WHERE site={site}")
    cursor.fetchall()

# fetchone() (returns None if no more rows available) and fetchmany(5) (returns max items as list)

# returns an iterable of type <class 'sqlite3.Cursor'>

# data = cursor.execute("SELECT * FROM credentials WHERE site='some_site'")
# print(type(data))  # <class 'sqlite3.Cursor'>
# print([item for item in data])
# [('some_site', 'user1', 'some_pass'), ('some_site', 'user1', 'some_pass')]


create_db_and_table()
insert_credential_into_table('some_site', 'user1', 'some_pass')
print(return_all_credentials())
conn.commit()
conn.close()


