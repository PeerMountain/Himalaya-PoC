import base64
from Crypto import Random
from Crypto.Cipher import AES as Base_AES


class AES():

    BLOCK_SIZE = 16
    KEY_SIZE = 32
    MODE = Base_AES.MODE_ECB

    def __init__(self, key):
        if(len(key) >= self.KEY_SIZE):
            raise Exception(
                'Key length must be equal to {0}.'.format(self.KEY_SIZE))
        
        self.key = self.__pad(key,self.KEY_SIZE)
        self.cipher = Base_AES.new(self.key, self.MODE)

    def __pad(self, s, l=BLOCK_SIZE):
        return s + (l - len(s) % l) * chr(l - len(s) % l).encode()

    def __unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]

    def encrypt(self, content):
        print(content.hex()+'1')
        local_content = self.__pad(content)
        print(local_content.hex()+'1')
        ciphed_content = self.cipher.encrypt(local_content)
        return base64.b64encode(ciphed_content)

    def decrypt(self, b64_ciphed_content):
        ciphed_content = base64.b64decode(b64_ciphed_content)
        content = self.cipher.decrypt(ciphed_content)
        return self.__unpad(content)
