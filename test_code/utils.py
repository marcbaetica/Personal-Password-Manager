import json
import subprocess


def retrieve_input_data():
    with open('test_code/credentials_for_testing.json', 'r') as f:
        return json.load(f)


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


def list_all_sites_and_credentials(credentials_list):
    print('\nListing all sites with credentials introduced in the db:')
    subprocess.run('python list_all_sites.py private_key')

    print('\nListing credentials:')
    for credentials in credentials_list:
        subprocess.run(f'python retrieve_credentials.py {credentials[0]} private_key')
    subprocess.run('python retrieve_credentials.py lalala private_key')


def add_credentials_to_db(credentials_to_add):
    print('\nAdding credentials to db:')
    for credentials in credentials_to_add:
        subprocess.run(f'python insert_credentials.py {credentials[0]} {credentials[1]} {credentials[2]} public_key')


def delete_credentials_from_db(credentials_to_delete):
    print('\nDeleting credentials from db:')
    for credentials in credentials_to_delete:
        subprocess.run(f'python delete_credentials.py {credentials[0]} {credentials[1]} public_key private_key')
