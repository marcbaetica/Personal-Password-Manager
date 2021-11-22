from lib.encryption import Encryption
from time import perf_counter

pub, priv = Encryption.generate_keys(4096, 4)

Encryption.save_key_to_file(pub, 'public_key')
Encryption.save_key_to_file(priv, 'private_key')
