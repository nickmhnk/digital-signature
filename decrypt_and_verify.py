import sys

from Crypto.PublicKey import RSA
from signature import sign, verify
from encryption import encrypt, decrypt

def pipeline(decrypt_key, verify_key, data, signature_length=128):
    try:
        decrypted = decrypt(decrypt_key, data)
    except:
        print("wrong")
        return
    verified = verify(verify_key, decrypted, signature_length=signature_length)
    if not verified:
        print("not verified")
        return

    res = decrypted[:-signature_length]
    return res


if __name__ == "__main__":
    with open('enc_key.pem', 'rb') as f:
        decrypt_key = f.read()

    with open('public_sign.pem', 'rb') as f:
        verify_key = RSA.importKey(f.read())

    with open('data.bin', 'rb') as f:
        data = f.read()

    res = pipeline(decrypt_key, verify_key, data)

    print(res)
