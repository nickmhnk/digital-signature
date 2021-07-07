from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import sys


with open('private.pem', 'rb') as f:
    key = RSA.importKey(f.read())

msg = sys.argv[1].encode()

msg_hash = SHA256.new(msg)
signer = PKCS1_v1_5.new(key)
signature = signer.sign(msg_hash)

with open('signed.bin', 'wb') as f:
    f.write(signature)
