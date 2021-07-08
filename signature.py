from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import sys


def sign(key, data):
    data_hash = SHA256.new(data)
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(data_hash)
    return signature


def verify(key, signed_data, signature_length=128):
    verifier = PKCS1_v1_5.new(key)

    data = signed_data[:-signature_length]
    signature = signed_data[-signature_length:]

    data_hash = SHA256.new(data)
    verified = verifier.verify(data_hash, signature)
    
    return verified


if __name__ == "__main__":
    with open('private_sign.pem', 'rb') as f:
        key = RSA.importKey(f.read())
    
    data = sys.argv[1].encode()

    signature = sign(key, data)

    signed_data = data + signature

    with open('public_sign.pem', 'rb') as f:
        verify_key = RSA.importKey(f.read())

    res = verify(verify_key, signed_data)

    print("good", res)

    bad = signed_data + b"asdf"


    res = verify(verify_key, bad)
    print("bad", res)
