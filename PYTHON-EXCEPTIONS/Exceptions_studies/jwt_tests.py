# encoding and decoding tokens with RS256 (RSA)

import jwt

private_key = b"-----BEGIN PRIVATE KEY-----\nMIGEAgEAMBAGByqGSM49AgEGBS..."
public_key = b"-----BEGIN PUBLIC KEY-----\nMHYwEAYHKoZIzj0CAQYFK4EEAC..."

encoded_jwt = jwt.encode({"chave": "payload"}, private_key, algorithm="RS256")
print("THIS IS THE ENCODED JWT: ", encoded_jwt)