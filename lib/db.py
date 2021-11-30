import os
import sqlite3
import sys

from lib.encryption import Encryption


class DB:
    def __init__(self, db_name='credentials.db'):
        self._db_name = db_name
        self._connection = self._create_db(db_name)
        self._cursor = self._connection.cursor()
        self._creds_table = 'credentials'
        self._sites_table = 'sites'
        self._create_table_if_not_exists(self._creds_table, self._sites_table)

    @staticmethod
    def _create_db(db_name):
        return sqlite3.connect(db_name)

    def _create_table_if_not_exists(self, creds_table, sites_table):
        with self._connection as conn:
            conn.execute(f'CREATE TABLE IF NOT EXISTS {creds_table} (hash TEXT, user TEXT, password TEXT)')
            conn.execute(f'CREATE TABLE IF NOT EXISTS {sites_table} (site TEXT)')

    def _list_table_columns(self):
        return self._cursor.execute('PRAGMA table_info("sqlite_master")').fetchall()

    def list_all_tables(self):
        tables = self._cursor.execute('SELECT * FROM sqlite_master WHERE type="table"').fetchall()
        return [table[1] for table in tables]

    def insert_credentials_into_db(self, cypher_credentials):
        with self._connection as conn:
            conn.execute(f'INSERT INTO {self._creds_table} VALUES (?, ?, ?)', (cypher_credentials.hashed_site,
                                                                               cypher_credentials.cypher_user,
                                                                               cypher_credentials.cypher_password))
            conn.execute(f'INSERT INTO sites VALUES (?)', (cypher_credentials.cypher_site,))

    def delete_credentials_from_db(self, site, user, private_key):
        cypher_sites = self._cursor.execute(f'SELECT * FROM sites').fetchall()
        sites = [Encryption.decrypt(site[0], private_key) for site in cypher_sites]
        if site not in sites:
            print(f'{site} was not found to be registered in the current list of existing sites: {sites}')
            print('No credentials will be removed.')
            sys.exit()  # Avoids printing the stack trace.
        cypher_users = self._cursor.execute(f'SELECT user FROM {self._creds_table} WHERE hash=?', (Encryption.hash_site(site),)).fetchall()
        users = [Encryption.decrypt(cypher_user[0], private_key) for cypher_user in cypher_users]
        if user not in users:
            print(f'Though the site {site} was found, no credential bearing user [{user}] was associated to that site.')
            print('No credentials will be removed.')
            sys.exit()
        with self._connection as conn:
            conn.execute(f'DELETE FROM {self._creds_table} WHERE hash=? AND user=?', (Encryption.hash_site(site), cypher_users[users.index(user)][0]))
            conn.execute(f'DELETE FROM {self._sites_table} WHERE site=?', (cypher_sites[sites.index(site)][0],))
            print('Deleted credentials!')


    def list_all_sites(self, private_key):
        sites = self._connection.execute('SELECT * FROM sites').fetchall()
        return [Encryption.decrypt(site[0], private_key) for site in sites]

    def return_all_credentials(self):
        """Retrieve all credentials from the database.

        :return: [List] The site and credentials as tuples in the format (site, user, password).
        """
        return self._connection.execute(f'SELECT * FROM {self._creds_table}').fetchall()

    def return_credentials_for_site(self, site, private_key):
        """Retrieve all credentials associated with a site.

        :param site: [String] The name of the site. Example: 'projecteuler.net'
        :param private_key: [PrivateKey] Private key used to decrypt the strings.
        :return: [List] The credentials as tuples in the format (user, password).
        """
        hashed_site = Encryption.hash_site(site)
        all_credentials = self._connection.execute(f'SELECT * FROM {self._creds_table} WHERE hash=?', (hashed_site,)).fetchall()
        credentials = [(Encryption.decrypt(credentials[1], private_key), Encryption.decrypt(credentials[2], private_key)) for credentials in all_credentials]
        return credentials if credentials else None

    def delete_db(self):
        self._connection.close()  # Otherwise PermissionError as process still uses db file.
        os.remove(self._db_name)


# NOTE: context managers avoid the need for connection.commit(). Not needed in the event of select.
# NOTE: (?), (some_var,) or (:name), ({'name': 'lala'}) is to prevent SQL injections if input comes from User.
# TODO: Update method for credentials.
