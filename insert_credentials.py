import sys
from lib.credentials import CypherCredentials
from lib.db import DB
from lib.load_keys import load_private_key_from_aws_secret, load_private_key_from_file


site = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
if len(sys.argv) == 5:
    if sys.argv[4].lower() == 'aws_key':
        print('Using private key from AWS Secret Manager.')  # TODO: Remove after testing.
        private_key = load_private_key_from_aws_secret()
    else:
        sys.exit(f'{sys.argv[4]} is not an acceptable value. Please use "aws_key" to pull keys from AWS Secrets Manager'
                 f' or nothing to use a local file defined in your .env.')
else:
    private_key = load_private_key_from_file()


db = DB()

# Insertion will not override credentials if they already exist in the db.
if not db.do_credentials_already_exist(site, user, private_key):
    new_cypher_creds = CypherCredentials(site, user, password)
    db.insert_credentials_into_db(new_cypher_creds)
    print(f'Inserted new credentials into db.')
else:
    print(f'Credentials associated with the {site}:{user} pair already exist in the db.'
          f' Try deleting them before attempting a new insertion.')
