import sys
from lib.db import DB
from lib.encryption import Encryption
from secret_hosting.private_key_retriever import get_secret


site = sys.argv[1]
# private_key = Encryption.load_private_key_from_file(sys.argv[2])
private_key = get_secret()  # TODO: toggle between AWS secrets and file on FS.


db = DB()
print(f'Credentials for site {site}: {db.return_credentials_for_site(site, private_key)}')
