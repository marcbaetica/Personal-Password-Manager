import boto3
from botocore.exceptions import ClientError
from pprint import pprint
from lib.encryption import Encryption


def get_secret(secret, region):
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


if __name__ == '__main__':
    secret_name = 'PasswordManagerAppKey'
    region_name = 'us-east-2'
    private_key = get_secret(secret_name, region_name)

    pprint(private_key)
    print(type(private_key))