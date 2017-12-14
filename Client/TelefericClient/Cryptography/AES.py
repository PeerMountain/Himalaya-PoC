import base64
from Crypto import Random
from Crypto.Cipher import AES as Base_AES


class AES():

    BLOCK_SIZE = 16
    KEY_SIZE = 32
    MODE = Base_AES.MODE_ECB

    def __init__(self, key):
        if type(key) is str:
            key = key.encode()
        key_length = len(key)
        if key_length > self.KEY_SIZE:
            raise Exception(
                'Key length must be lower or equal to {0}.'.format(self.KEY_SIZE))
        elif key_length < self.KEY_SIZE:
            self.key = self.pad(key,self.KEY_SIZE)
        else:
            self.key = key
        self.cipher = Base_AES.new(self.key, self.MODE)

    @classmethod
    def pad(self, s, l=BLOCK_SIZE):
        if len(s) % l is 0:
            return s
        diff = l - len(s) % l
        return s + (diff) * chr(diff).encode()

    @classmethod
    def unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]

    def encrypt(self, content):
        local_content = self.pad(content)
        ciphed_content = self.cipher.encrypt(local_content)
        return base64.b64encode(ciphed_content)

    def decrypt(self, b64_ciphed_content):
        ciphed_content = base64.b64decode(b64_ciphed_content)
        content = self.cipher.decrypt(ciphed_content)
        return self.unpad(content)
