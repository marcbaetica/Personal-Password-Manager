import rsa


class Encryption:
    @staticmethod
    def generate_keys(nbits=882):
        # 82 bits are used as buffer by rsa
        # The remaining 800 bits (100 bytes) will allow encryption of a strings of up to 100 characters.
        # Anything under 16 bits will throw ValueError.
        return rsa.newkeys(nbits)

    @staticmethod
    def encrypt(message, pub_key):
        return rsa.encrypt(message.encode(), pub_key)

    @staticmethod
    def decrypt(crypto, priv_key):
        return rsa.decrypt(crypto, priv_key).decode()
