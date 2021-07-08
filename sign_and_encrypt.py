import sys
from Crypto.PublicKey import RSA
from signature import sign
from encryption import encrypt

if __name__ == "__main__":
    with open('private_sign.pem', 'rb') as f:
        key = RSA.importKey(f.read())

    data = sys.argv[1].encode()

    signature = sign(key, data)

    signed_data = data + signature


    with open('enc_key.pem', 'rb') as f:
        encrypt_key = f.read()

    cipher_text = encrypt(encrypt_key, signed_data)

    with open("data.bin", "wb") as f:
        f.write(cipher_text)
