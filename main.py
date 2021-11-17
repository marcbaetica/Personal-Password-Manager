from lib.encryption import Encryption



message = 'Hello'
pub, priv = Encryption.generate_keys(512)
crypto = Encryption.encrypt(message, pub)
decrypted = Encryption.decrypt(crypto, priv)

print(message)
print(crypto.hex())
print(decrypted)
