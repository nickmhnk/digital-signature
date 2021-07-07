from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import sys


with open('public.pem', 'rb') as f:
    key = RSA.importKey(f.read())

msg = sys.argv[1].encode() 
msg_hash = SHA256.new(msg)
verifier = PKCS1_v1_5.new(key)

with open('signed.bin', 'rb') as f:
    signature = f.read()

verified = verifier.verify(msg_hash, signature)

print(verified)
