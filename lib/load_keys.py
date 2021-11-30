import boto3
import os
import sys
from botocore.exceptions import ClientError
from dotenv import load_dotenv
from lib.encryption import Encryption


load_dotenv()
secret_name = os.getenv('secret_name')
region_name = os.getenv('secret_region')
# TODO: If any env vars return None, sys exit here rather than elsewhere (methods below).


def load_public_key_from_file():
    public_key_location = os.getenv('public_key_location')
    if public_key_location is None:
        sys.exit(f'Could not parse location of public key. Check that .env variables are correct.'
                 f' Current value: {public_key_location}')
    return Encryption.load_public_key_from_file(public_key_location)


def load_private_key_from_file():
    private_key_location = os.getenv('private_key_location')
    if private_key_location is None:
        sys.exit(f'Could not parse location of private key. Check that .env variables are correct.'
                 f' Current value: {private_key_location}')
    return Encryption.load_private_key_from_file(private_key_location)


def load_private_key_from_aws_secret(secret=secret_name, region=region_name):
    if secret_name is None or region_name is None:
        sys.exit('Could not parse variable for secret name or region. Check that .env variables are correct.'
                 f' Current values are: secret={secret_name} region={region_name}')

    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret)
    except ClientError as e:
        if e.response['Error']['Code'] == 'InternalServiceErrorException':
            raise ValueError('An error occurred on the server side.')
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            raise ResourceWarning(f'Could not find any secret {secret} under region {region}.')
    else:
        if 'SecretString' in get_secret_value_response:
            return Encryption.load_private_key_from_text(get_secret_value_response['SecretString'])

