import sys

from pprintpp import pprint

from lib.db import DB
from lib.encryption import Encryption


private_key = Encryption.load_private_key_from_file(sys.argv[1])

db = DB()
print('Sites currently in the DB:')
pprint(db.list_all_sites(private_key))