import json


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
