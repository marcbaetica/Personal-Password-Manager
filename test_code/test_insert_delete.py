import subprocess
from pprintpp import pprint
from lib.db import DB


from test_code.utils import retrieve_input_data, parse_credentials,\
    add_credentials_to_db, list_all_sites_and_credentials, delete_credentials_from_db


test_data = retrieve_input_data()
items_to_add = [parse_credentials(item) for item in test_data['to_add']]
items_to_modify_before_delete = [parse_credentials(item) for item in test_data['to_modify_before_delete']]
items_to_delete = [parse_credentials(item) for item in test_data['to_delete']]
items_to_modify_after_delete = [parse_credentials(item) for item in test_data['to_modify_after_delete']]

# pprint(items_to_add)
# pprint(items_to_modify_before_delete)
# pprint(items_to_delete)
# pprint(items_to_modify_after_delete)


subprocess.run('python --version')
# subprocess.run('python generate_keys.py')  # Takes 1 minute to generate the 4096-bit keys.


add_credentials_to_db(items_to_add, True)
list_all_sites_and_credentials(items_to_add)
delete_credentials_from_db(items_to_delete)
add_credentials_to_db(items_to_add)
list_all_sites_and_credentials(items_to_add, True)
delete_credentials_from_db(items_to_delete, True)
add_credentials_to_db(items_to_add, True)
list_all_sites_and_credentials(items_to_add, True)

db = DB()
db.delete_db()
