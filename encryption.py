import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES  
from cryptography.fernet import Fernet

IV = "asdfasdfasdfasdf"

def encrypt(key, data):
    cipher = Fernet(key) 
    return cipher.encrypt(data)


def decrypt(key, data):
    decipher = Fernet(key) 
    return decipher.decrypt(data) 


if __name__ == "__main__":

    with open('enc_key.pem', 'rb') as f:
        key = f.read()

    data = sys.argv[1].encode()

    print(data)
    cipher_text = encrypt(key, data)
    res = decrypt(key, cipher_text)
    print(res)


