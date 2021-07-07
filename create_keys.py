from Crypto.PublicKey import RSA
private_key = RSA.generate(1024)
public_key = private_key.publickey()

with open ("private.pem", "wb") as prv_file:
    prv_file.write(private_key.exportKey())

with open ("public.pem", "wb") as pub_file:
    pub_file.write(public_key.exportKey())

