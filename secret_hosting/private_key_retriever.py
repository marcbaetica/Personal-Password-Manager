import boto3
import os
import sys
from botocore.exceptions import ClientError
from dotenv import load_dotenv
from lib.encryption import Encryption


load_dotenv()
secret_name = os.getenv('secret_name')
region_name = os.getenv('secret_region')
if secret_name is None or region_name is None:
    sys.exit('Could not parse variable for secret name or region. Check that .env variables are correct.'
             f' Current values are: secret={secret_name} region={region_name}')


def get_secret(secret=secret_name, region=region_name):
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
