import rsa


class Encryption:
    @staticmethod
    def generate_keys(nbits):
        return rsa.newkeys(nbits)

    @staticmethod
    def encrypt(message, pub_key):
        return rsa.encrypt(message.encode(), pub_key)

    @staticmethod
    def decrypt(crypto, priv_key):
        return rsa.decrypt(crypto, priv_key).decode()
