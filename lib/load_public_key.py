import sys
import os
from dotenv import load_dotenv
from lib.encryption import Encryption


load_dotenv()


def load_public_key():
    public_key_location = os.getenv('public_key_location')
    if public_key_location is None:
        sys.exit(f'Could not parse location of public key. Check that .env variables are correct.'
                 f' Current value: {public_key_location}')
    return Encryption.load_public_key_from_file(public_key_location)
