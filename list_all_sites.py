import sys
from lib.db import DB
from lib.encryption import Encryption
from pprintpp import pprint
from secret_hosting.private_key_retriever import get_secret


# private_key = Encryption.load_private_key_from_file(sys.argv[1])
private_key = get_secret()  # TODO: toggle between AWS secrets and file on FS.


db = DB()
print('Sites currently in the DB:')
pprint(db.list_all_sites(private_key))