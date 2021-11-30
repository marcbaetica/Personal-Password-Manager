import sys
from lib.credentials import CypherCredentials
from lib.db import DB
from lib.encryption import Encryption
from secret_hosting.private_key_retriever import get_secret


site = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
# private_key = Encryption.load_private_key_from_file(sys.argv[4])
private_key = get_secret()  # TODO: toggle between AWS secrets and file on FS.


db = DB()

# Insertion will not override credentials if they already exist in the db.
if not db.do_credentials_already_exist(site, user, private_key):
    new_cypher_creds = CypherCredentials(site, user, password)
    db.insert_credentials_into_db(new_cypher_creds)
    print(f'Inserted new credentials into db.')
else:
    print(f'Credentials associated with the {site}:{user} pair already exist in the db.'
          f' Try deleting them before attempting a new insertion.')
