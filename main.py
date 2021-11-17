from lib.encryption import Encryption



message = 'Hello'
# pub, priv = Encryption.generate_keys(512)
# print(pub.save_pkcs1())
# print(priv.save_pkcs1())
#
# crypto = Encryption.encrypt(message, pub)
# decrypted = Encryption.decrypt(crypto, priv)
#
# print(message)
# print(crypto.hex())
# print(decrypted)


def run_permutation(message, nbits):
    pub, priv = Encryption.generate_keys(nbits)
    # print(len(pub.save_pkcs1().decode()))
    # print(priv.save_pkcs1())

    crypto = Encryption.encrypt(message, pub)
    decrypted = Encryption.decrypt(crypto, priv)

    print(message)
    print(crypto.hex())
    print(decrypted)


import string
from random import choice


message = ''.join([choice(string.ascii_uppercase) for _ in range(100)])
print(message)
for i in range(870, 890):
    try:
        run_permutation(message, i)
        print(f'Number of bits: {i}')
    except ValueError:
        print(f'{i} not acceptable.')
    except OverflowError as e:
        print(f'{i} not acceptable. Overflow error: {e}')


# 15 not acceptable.
# 16 not acceptable. Overflow error: 0 bytes needed for message, but there is only space for -9
#  -> 0 chars, 82 bits key (10.25 bytes)
# H -> 1 char, 90 bits key (11.25 bytes)
# He -> 2 chars, 98 bits key (12.25 bytes)
# Hel -> 3 chars, 106 bits key (13.25 bytes)
# Hell -> 4 chars, 114 bits key (14.25 bytes)
# Hello -> 5 chars, 122 bits key (15.25 bytes)
# 4096 n-bits => 501 chars max.
# 100 chars + 10.25 buffer = 110.25 chars. 110.25 * 8 bits = 882 bits will encrypt strings of up to 100 characters.