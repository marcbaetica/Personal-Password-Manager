import sys

from lib.credentials import Credentials
from lib.db import DB


site = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]

new_cred = Credentials(site, user, password)
# TODO: error handling with improper input

db = DB()
db.insert_credentials_into_table(new_cred)
print(f'Inserted new credentials into db.')

# TODO: remove this!
print(db.return_credentials_from_site(site))
