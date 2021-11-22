# Personal Password Manager

Keep track of your passwords locally. The storage medium is a db file that you can take with you on the go. All entities
(site, username, password) are asynchronously encrypted using powerful 4096-bit keys as to not allow any intrusion.
Anyone with the public key can insert credentials into the db, while only the true owner can read valuable information 
from the DB through the use of the private key.

#### How to use:
First, the keys must be generated:  
`python3 generate_keys.py`  
NOTE: make sure to move the private keys to a different location. Whoever has this, can access your full list of credentials.

To insert credentials run:  
`python3 insert_credentials.py site username password path_to_public_key`

To retrieve credentials associated to a particular site run:  
`python3 retrieve_credentials.py site path_to_private_key`