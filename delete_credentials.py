import sys
from lib.db import DB
from lib.encryption import Encryption


site = sys.argv[1]
user = sys.argv[2]
public_key = Encryption.load_public_key_from_file(sys.argv[3])
private_key = Encryption.load_private_key_from_file(sys.argv[4])

# look up encrypted site in sites table. If not exists, print site not exists error and sys.exit() -> avoiding trace
db = DB()
sites = db.list_all_sites(private_key)

db.delete_credentials_from_db(site, user, public_key, private_key)

# look up hash site and user in credentials table. if not exist print user not exists error and sys.exit()
# delete entry in credentials table and delete entry in sites table



