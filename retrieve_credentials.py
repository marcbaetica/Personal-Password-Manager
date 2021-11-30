import sys
from lib.db import DB
from lib.load_keys import load_private_key_from_file, load_private_key_from_aws_secret


site = sys.argv[1]
if len(sys.argv) == 3:
    if sys.argv[2].lower() == 'aws_key':
        print('Using private key from AWS Secret Manager.')  # TODO: Remove after testing.
        private_key = load_private_key_from_aws_secret()
    else:
        sys.exit(f'{sys.argv[2]} is not an acceptable value. Please use "aws_key" to pull keys from AWS Secrets Manager'
                 f' or nothing to use a local file defined in your .env.')
else:
    private_key = load_private_key_from_file()


db = DB()
print(f'Credentials for site {site}: {db.return_credentials_for_site(site, private_key)}')
