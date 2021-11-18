import rsa


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
        return rsa.decrypt(crypto, priv_key).decode()

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
