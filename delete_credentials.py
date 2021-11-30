import sys
from lib.db import DB
from lib.encryption import Encryption


site = sys.argv[1]
user = sys.argv[2]
public_key = Encryption.load_public_key_from_file(sys.argv[3])
private_key = Encryption.load_private_key_from_file(sys.argv[4])

db = DB()
sites = db.list_all_sites(private_key)

db.delete_credentials_from_db(site, user, private_key)



