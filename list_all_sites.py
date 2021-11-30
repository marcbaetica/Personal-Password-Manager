import sys
from lib.db import DB
from lib.encryption import Encryption
from lib.load_keys import load_private_key_from_aws_secret
from pprintpp import pprint


# private_key = Encryption.load_private_key_from_file(sys.argv[1])
private_key = load_private_key_from_aws_secret()  # TODO: toggle between AWS secrets and file on FS.


db = DB()
print('Sites currently in the DB:')
pprint(db.list_all_sites(private_key))