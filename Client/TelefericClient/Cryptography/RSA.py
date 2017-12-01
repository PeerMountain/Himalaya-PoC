from Crypto.PublicKey import RSA as Key
from Crypto.PublicKey.RSA import _RSAobj
from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto import Random
from Crypto.Hash import SHA256

import base64


class RSA():

    def __init__(self, key):
        key_type = type(key)
        if key_type == str or key_type == bytes:
            self.key = Key.importKey(key)
        elif key_type == _RSAobj:
            self.key = key
        else:
            raise Exception('Invalid key format.')

    def encrypt(self, content):
        cyphred_content = self.key.encrypt(content, None)
        return base64.b64encode(cyphred_content[0])

    def decrypt(self, b64_ciphred_content):
        ciphred_content = base64.b64decode(b64_ciphred_content)
        return self.key.decrypt(ciphred_content)

    def sign(self, content):
        content_hash = SHA256.new(content).digest()
        signature = self.key.sign(content_hash, None)
        bytes_signature = long_to_bytes(signature[0])
        return base64.b64encode(bytes_signature)

    def verify(self, content, b64_bytes_signature):
        content_hash = SHA256.new(content).digest()
        bytes_signature = base64.b64decode(b64_bytes_signature)
        signature = bytes_to_long(bytes_signature)
        return self.key.verify(content_hash, [signature])
