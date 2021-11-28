import json
import subprocess
from pprintpp import pprint
from lib.encryption import Encryption
from lib.db import DB


from test_code.utils import retrieve_input_data, parse_credentials


test_data = retrieve_input_data()
items_to_add = [parse_credentials(item) for item in test_data['to_add']]
items_to_modify_before_delete = [parse_credentials(item) for item in test_data['to_modify_before_delete']]
items_to_delete = [parse_credentials(item) for item in test_data['to_delete']]
items_to_modify_after_delete = [parse_credentials(item) for item in test_data['to_modify_after_delete']]

# pprint(items_to_add)
# pprint(items_to_modify_before_delete)
# pprint(items_to_modify_before_delete)
# pprint(items_to_modify_after_delete)


subprocess.run('python --version')
# subprocess.run('python generate_keys.py')  # Takes 1 minute to generate the 4096-bit keys.

print()

for credentials in items_to_add:
    subprocess.run(f'python insert_credentials.py {credentials[0]} {credentials[1]} {credentials[2]} public_key')

print()

subprocess.run('python list_all_sites.py private_key')

print()

subprocess.run('python retrieve_credentials.py www.facebook.com public_key private_key')
subprocess.run('python retrieve_credentials.py lalala public_key private_key')

db = DB()
db.delete_db()
