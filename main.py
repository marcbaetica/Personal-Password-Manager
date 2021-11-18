from lib.encryption import Encryption


message = 'Hello'
pub, priv = Encryption.generate_keys()
print(Encryption.get_key_as_string(pub))
print(Encryption.get_key_as_string(priv))

Encryption.save_key_to_file(pub, 'public_key')
print(Encryption.load_key_from_file('public_key'))

Encryption.save_key_to_file(priv, 'private_key')
print(Encryption.load_key_from_file('private_key'))

crypto = Encryption.encrypt(message, pub)
decrypted = Encryption.decrypt(crypto, priv)

print(message)
print(crypto.hex())
print(decrypted)
