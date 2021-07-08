from Crypto.PublicKey import RSA
from cryptography.fernet import Fernet

# one pair for signing
private_key = RSA.generate(1024)
public_key = private_key.publickey()

with open ("private_sign.pem", "wb") as prv_file:
    prv_file.write(private_key.exportKey())

with open ("public_sign.pem", "wb") as pub_file:
    pub_file.write(public_key.exportKey())


key = Fernet.generate_key() 

with open ("enc_key.pem", "wb") as f:
    f.write(key)

