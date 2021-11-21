import rsa
from rsa.pkcs1 import DecryptionError, VerificationError


class Encryption:
    @staticmethod
    def generate_keys(nbits=882):
        # 82 bits are used as buffer by rsa
        # The remaining 800 bits (100 bytes) will allow encryption of a strings of up to 100 characters.
        # Anything under 16 bits will throw ValueError: Key too small.
        # Anything from 16 bits and under 82 bits will raise:
        # OverflowError: X bytes needed for message (your char count), but there is only space for -9 (at 16) -1 (at 81)
        return rsa.newkeys(nbits)

    @staticmethod
    def encrypt(message, pub_key):
        return rsa.encrypt(message.encode(), pub_key)

    @staticmethod
    def decrypt(crypto, priv_key):
        try:
            decrypted_message = rsa.decrypt(crypto, priv_key)
        except DecryptionError as e:  # Hiding stack traces to prevent vulnerabilities exploitation.
            raise SystemExit(f'Failed to decrypt message. Perhaps message contents have been tampered with? Error: {e}')
        return decrypted_message.decode()

    @staticmethod
    def get_key_as_string(key):
        return key.save_pkcs1().decode()

    @classmethod
    def save_key_to_file(cls, key, name):
        with open(f'{name}', 'w') as f:
            f.write(cls.get_key_as_string(key))

    @staticmethod
    def load_key_from_file(name):
        with open(f'{name}', 'r') as f:
            return f.read()


# TODO: remove this or change to tests.
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

# Breaking message (with hiding stack trace).
print(crypto)
crypto = crypto[:-1]
print(crypto)
decrypted = Encryption.decrypt(crypto, priv)

print(message)
print(crypto.hex())
print(decrypted)
