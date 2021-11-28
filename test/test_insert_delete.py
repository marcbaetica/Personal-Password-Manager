import json
import subprocess
from pprintpp import pprint
from lib.encryption import Encryption
from lib.db import DB


with open('test/credentials_for_testing.json', 'r') as f:
    test_data = json.load(f)

pprint(test_data)
print(type(test_data['to_add']))


def parse_credentials(credentials):
    """Takes credentials and parses them."""
    site, user, password = None, None, None
    for cred in credentials:
        site = cred['site'] if 'site' in cred.keys() else site
        user = cred['user'] if 'user' in cred.keys() else user
        password = cred['pass'] if 'pass' in cred.keys() else password
    if not password:  # Credentials for deletion query don't contain passwords.
        return site, user
    return site, user, password


[print(parse_credentials(creds)) for creds in test_data['to_add']]
[print(parse_credentials(creds)) for creds in test_data['to_modify_before_delete']]
[print(parse_credentials(creds)) for creds in test_data['to_delete']]
[print(parse_credentials(creds)) for creds in test_data['to_modify_after_delete']]


"""
subprocess.run('python --version')
# subprocess.run('python generate_keys.py')  # Takes 1 minute to generate the 4096-bit keys.

print()

subprocess.run('python insert_credentials.py some_site_1 some_user_1 some_password_1 public_key')
subprocess.run('python insert_credentials.py some_site_2 some_user_2 some_password_2 public_key')
subprocess.run('python insert_credentials.py some_site_3 some_user_3 some_password_3 public_key')
subprocess.run('python insert_credentials.py some_site_4 some_user_4 some_password_4 public_key')

print()

subprocess.run('python list_all_sites.py private_key')

print()

subprocess.run('python retrieve_credentials.py some_site_1 public_key private_key')    # [('some_user_1', 'some_password_1')]
subprocess.run('python retrieve_credentials.py lalala public_key private_key')         # []

db = DB()
db.delete_db()
"""