from lib.encryption import Encryption
from lib.load_keys import load_public_key_from_file


public_key = load_public_key_from_file()


class CypherCredentials:
    def __init__(self, site, user, password):
        self.hashed_site = Encryption.hash_site(site)
        self.cypher_site = Encryption.encrypt(site, public_key)
        self.cypher_user = Encryption.encrypt(user, public_key)
        self.cypher_password = Encryption.encrypt(password, public_key)

    def __repr__(self):
        return f'CypherCredentials({self.cypher_site}, {self.cypher_user}, {self.cypher_password})'
