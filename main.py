from pprintpp import pprint

from lib.credentials import Credentials
from lib.db import DB


cred_1 = Credentials('ottawa.bibliocommons.com', 'alexandria', 'red_em_all')
cred_2 = Credentials('projecteuler.net', 'smarty_pants', 'i_am_the_best')
cred_3 = Credentials('steam.com', 'gamer1', 'strong_password')

db = DB('credentials.db')
print(f'All tables: {db.list_all_tables()}')

print(db.return_all_credentials())
print(db.insert_credentials_into_table(cred_1))
print(db.insert_credentials_into_table(cred_2))
print(db.insert_credentials_into_table(cred_3))
pprint(db.return_all_credentials())

db.return_credentials_for_site('ottawa.bibliocommons.com')
db.return_credentials_for_site('ottawa.bibliocommonZ.com')

db.delete_db()

# TODO: handle if credential query returns empty list.
