# Personal Password Manager

Keep track of your passwords locally. The storage medium is a db file that you can take with you on the go. All entities
(site, username, password) are asynchronously encrypted using powerful 4096-bit keys as to not allow any intrusion.
Anyone with the public key can insert credentials into the db, while only the true owner can read valuable information 
from the DB through the use of the private key. Credentials are indexed by a hash of the site byte string and are added
to a different db table than the one containing the sites. This serves two purposes: a deterministic lookup (unlike
encrypting, hashing output is always deterministic) and also as an extra minimum layer of added security. Thus, anyone
with the db file can not read its contents without the private key, however (hypothetically) in an extreme scenario where
the private key were stolen, the separation of sites from the credentials adds an extra block in the way as the attacker
does not know the hashing algorithm that was used or what was hashed in the first place.

#### How to use:
First, the keys must be generated (the large keys take a minute to generate):  
`python3 generate_keys.py`  
NOTE: make sure to move the private keys to a different location. Whoever has this, can decrypt your full list of credentials.

To insert credentials run:  
`python3 insert_credentials.py site username password path_to_public_key`

To view the list of sites that contain credentials:  
`python list_all_sites.py path_to_private_key`

To retrieve credentials associated to a particular site run:  
`python3 retrieve_credentials.py site path_to_private_key`  
NOTE: An empty list will be returned