import sys

from lib.db import DB


site = sys.argv[1]

db = DB()
print(db.return_credentials_from_site(site))

# TODO: Convert POC into actual implementation.
from lib.encryption import Encryption
private_key = Encryption.load_private_key_from_file('private_key')

print([(Encryption.decrypt(item[0], private_key), Encryption.decrypt(item[1], private_key)) for item in db.return_all_credentials()])
