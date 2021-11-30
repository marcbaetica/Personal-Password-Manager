import os
import sys
from dotenv import load_dotenv
from lib.credentials import CypherCredentials
from lib.db import DB
from lib.encryption import Encryption
from secret_hosting.private_key_retriever import get_secret


load_dotenv()

# TODO: find which returns None by default.
secret_name = os.environ.get('secret_name')
secret_region = os.getenv('secret_region')

site = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
private_key = get_secret(secret_name, secret_region)  # TODO: toggle between AWS secrets and file on FS.

db = DB()

# Check if credentials for site-user pair already exist.
if not db.do_credentials_already_exist(site, user, private_key):
    new_cypher_creds = CypherCredentials(site, user, password)
    db.insert_credentials_into_db(new_cypher_creds)
    print(f'Inserted new credentials into db.')
else:
    print(f'Credentials associated with the {site}:{user} pair already exist in the db.'
          f' Try deleting them before attempting a new insertion.')
