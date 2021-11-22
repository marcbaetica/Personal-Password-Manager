import subprocess

from lib.encryption import Encryption
from lib.db import DB


subprocess.run('python --version')
# subprocess.run('python generate_keys.py')

print()

subprocess.run('python insert_credentials.py some_site_1 some_user_1 some_password_1 public_key')
subprocess.run('python insert_credentials.py some_site_2 some_user_2 some_password_2 public_key')
subprocess.run('python insert_credentials.py some_site_3 some_user_3 some_password_3 public_key')
subprocess.run('python insert_credentials.py some_site_4 some_user_4 some_password_4 public_key')

print()

subprocess.run('python retrieve_credentials.py some_site_1')    # [('some_user_1', 'some_password_1')]
subprocess.run('python retrieve_credentials.py lalala')         # []

db = DB()
db.delete_db()
