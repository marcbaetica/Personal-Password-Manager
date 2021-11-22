import os
import sqlite3

from lib.encryption import Encryption


class DB:
    def __init__(self, db_name='credentials.db'):
        self._db_name = db_name
        self._connection = self._create_db(db_name)
        self._cursor = self._connection.cursor()
        self._table = 'credentials'
        self._create_table_if_not_exists(self._table)

    @staticmethod
    def _create_db(db_name):
        return sqlite3.connect(db_name)

    def _create_table_if_not_exists(self, table):
        with self._connection as conn:
            conn.execute(f'CREATE TABLE IF NOT EXISTS {table} (hash TEXT, user TEXT, password TEXT)')
            conn.execute(f'CREATE TABLE IF NOT EXISTS sites (site TEXT)')

    def _list_table_columns(self):
        return self._cursor.execute('PRAGMA table_info("sqlite_master")').fetchall()

    def list_all_tables(self):
        tables = self._cursor.execute('SELECT * FROM sqlite_master WHERE type="table"').fetchall()
        return [table[1] for table in tables]

    def insert_credentials_into_table(self, credentials, public_key):
        hashed_site = Encryption.hash_site(credentials.site)
        cypher_site = Encryption.encrypt(credentials.site, public_key)
        cypher_user = Encryption.encrypt(credentials.user, public_key)
        cypher_password = Encryption.encrypt(credentials.password, public_key)
        with self._connection as conn:
            conn.execute(f'INSERT INTO {self._table} VALUES (?, ?, ?)', (hashed_site, cypher_user, cypher_password))
            conn.execute(f'INSERT INTO sites VALUES (?)', (cypher_site,))

    def list_all_sites(self, private_key):
        sites = self._connection.execute('SELECT * FROM sites').fetchall()
        return [Encryption.decrypt(site[0], private_key) for site in sites]

    def return_all_credentials(self):
        """Retrieve all credentials from the database.

        :return: [List] The site and credentials as tuples in the format (site, user, password).
        """
        return self._connection.execute(f'SELECT * FROM {self._table}').fetchall()

    def return_credentials_for_site(self, site, private_key):
        """Retrieve all credentials associated with a site.

        :param site: [String] The name of the site. Example: 'projecteuler.net'
        :return: [List] The credentials as tuples in the format (user, password).
        """
        hashed_site = Encryption.hash_site(site)
        all_credentials = self._connection.execute(f'SELECT * FROM {self._table} WHERE hash=?', (hashed_site,)).fetchall()
        return [(Encryption.decrypt(credentials[1], private_key), Encryption.decrypt(credentials[2], private_key)) for credentials in all_credentials]

    def delete_db(self):
        self._connection.close()  # Otherwise PermissionError as process still uses db file.
        os.remove(self._db_name)


# NOTE: context managers avoid the need for connection.commit(). Not needed in the event of select.
# NOTE: (?), (some_var,) or (:name), ({'name': 'lala'}) is to prevent SQL injections if input comes from User.
# TODO: Update and delete methods for credentials.
