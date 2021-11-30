import sys
from lib.db import DB
from lib.load_keys import load_public_key_from_file, load_private_key_from_file, load_private_key_from_aws_secret


site = sys.argv[1]
user = sys.argv[2]
public_key = load_public_key_from_file()
if len(sys.argv) == 4:
    if sys.argv[3].lower() == 'aws_key':
        print('Using private key from AWS Secret Manager.')  # TODO: Remove after testing.
        private_key = load_private_key_from_aws_secret()
    else:
        sys.exit(f'{sys.argv[3]} is not an acceptable value. Please use "aws_key" to pull keys from AWS Secrets Manager'
                 f' or nothing to use a local file defined in your .env.')
else:
    private_key = load_private_key_from_file()


db = DB()

sites = db.list_all_sites(private_key)
db.delete_credentials_from_db(site, user, private_key)
