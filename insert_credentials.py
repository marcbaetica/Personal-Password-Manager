import sys

from lib.credentials import Credentials
from lib.db import DB
from lib.encryption import Encryption


site = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
public_key = Encryption.load_public_key_from_file(sys.argv[4])  # TODO: Make read file location not file name.

new_cred = Credentials(site, user, password)

db = DB()
db.insert_credentials_into_table(new_cred, public_key)
print(f'Inserted new credentials into db.')
