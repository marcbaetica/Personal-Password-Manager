import sys

from lib.db import DB
from lib.encryption import Encryption


site = sys.argv[1]
public_key = Encryption.load_public_key_from_file(sys.argv[2])
private_key = Encryption.load_private_key_from_file(sys.argv[3])

db = DB()
print(f'Credentials for site {site}: {db.return_credentials_for_site(site, private_key)}')
