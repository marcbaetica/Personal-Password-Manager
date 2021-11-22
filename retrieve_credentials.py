import sys

from lib.db import DB


site = sys.argv[1]

print(site)

db = DB()
print(db.return_all_credentials())
print(db.return_credentials_from_site(site))
