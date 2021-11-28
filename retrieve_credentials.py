import sys

from lib.db import DB
from lib.encryption import Encryption


site = sys.argv[1]
private_key = Encryption.load_private_key_from_file(sys.argv[2])

db = DB()
print(f'Credentials for site {site}: {db.return_credentials_for_site(site, private_key)}')
