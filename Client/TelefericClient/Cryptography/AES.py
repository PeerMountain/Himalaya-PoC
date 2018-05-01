import logging
import random
import sys
import base64
from typing import Union

from Cryptodome import Random
from Cryptodome.Cipher import AES as Base_AES


logger = logging.getLogger(__name__)


class AES:
    """AES

    Helper class for AES, using GCM mode.
    """

    def __init__(self, key: bytes, nonce: Union[bytes, None]=None):
        """__init__
        Initialize the cipher.
        :param key: Encryption or decryption key.
        :type key: bytes
        :param nonce: Nonce to be used in encryption or decryption.
            If no nonce is supplied, a random one WILL be generated.
        :type nonce: Union[bytes, None]
        """
        self.nonce = (
            nonce if nonce
            else bytes(random.randint(1, 255) for _ in range(16))
        )
        self.key = key
        self.cipher = Base_AES.new(key, Base_AES.MODE_GCM, nonce=self.nonce)

    def decrypt(self, ciphertext: bytes, tag: Union[bytes, None]=None) -> bytes:
        """decrypt
        Decrypt a piece of ciphertext.
        :param ciphertext: Base64 encoded ciphertext to decrypt.
        :type ciphertext: bytes
        :param tag: Base64 encoded tag to be used for message authentication.
            If no tag is supplied, authentication WILL NOT be performed.
        :type tag: Union[bytes, None]
        :rtype: bytes
        """
        decoded_ciphertext = base64.b64decode(ciphertext)
        plaintext = self.cipher.decrypt(decoded_ciphertext)
        if not tag:
            logger.warning("Tag not supplied, skipping message authentication.")
            return plaintext
        try:
            self.cipher.verify(
                base64.b64decode(tag)
            )
            logger.debug("AES tag verified successfully!")
            return plaintext
        except ValueError:
            logger.error(
                "AES tag could not be verfied."
                " Key incorrect or message corrupted."
            )
            return None

    def encrypt(self, data: bytes) -> bytes:
        """encrypt
        Encrypt a piece of data.
        :param data: Data to be encrypted.
        :type data: bytes
        :rtype: bytes
        """
        ciphertext, _ = self.cipher.encrypt_and_digest(data)
        return base64.b64encode(ciphertext)


# TODO: replace with correct AES encryption scheme from pycryptodome
class AESOld():
    """AES

    AES algorithm implementation.
    """

    BLOCK_SIZE = 16
    KEY_SIZE = 32
    MODE = Base_AES.MODE_ECB

    def __init__(self, key):
        key_length = len(key)
        if key_length > self.KEY_SIZE:
            raise Exception(
                'Key length must be lower or equal to {0}.'.format(self.KEY_SIZE))
        elif key_length < self.KEY_SIZE:
            self.key = self.__pad(key,self.KEY_SIZE)
        else:
            self.key = key
        self.cipher = Base_AES.new(self.key, self.MODE)

    def __pad(self, s, l=BLOCK_SIZE):
        return s + (l - len(s) % l) * chr(l - len(s) % l).encode()

    def __unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]

    def encrypt(self, content):
        local_content = self.__pad(content)
        ciphed_content = self.cipher.encrypt(local_content)
        return base64.b64encode(ciphed_content)

    def decrypt(self, b64_ciphed_content):
        ciphed_content = base64.b64decode(b64_ciphed_content)
        content = self.cipher.decrypt(ciphed_content)
        return self.__unpad(content)
