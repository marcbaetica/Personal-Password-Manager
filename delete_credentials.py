import sys
from lib.db import DB
from lib.encryption import Encryption
from lib.load_keys import load_public_key_from_file, load_private_key_from_aws_secret


site = sys.argv[1]
user = sys.argv[2]
public_key = load_public_key_from_file()
# private_key = Encryption.load_private_key_from_file(sys.argv[4])
private_key = load_private_key_from_aws_secret()  # TODO: toggle between AWS secrets and file on FS.


db = DB()

sites = db.list_all_sites(private_key)
db.delete_credentials_from_db(site, user, private_key)



