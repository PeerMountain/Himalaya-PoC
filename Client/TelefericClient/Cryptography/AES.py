import logging
import random
import sys
import base64
from typing import Union

from Cryptodome import Random
from Cryptodome.Cipher import AES as Base_AES
from Cryptodome.Util import Padding


logger = logging.getLogger(__name__)


class AES:
    """AES

    Helper class for AES, using ECB mode.
    """

    BLOCK_SIZE = 16
    KEY_SIZE = 32

    def __init__(self, key: bytes):
        """__init__
        Initialize the cipher.
        :param key: Encryption or decryption key.
        :type key: bytes
        """
        if not isinstance(key, bytes):
            key = key.encode()
        _key = Padding.pad(key,block_size=self.KEY_SIZE)
        self.cipher = Base_AES.new(_key, Base_AES.MODE_ECB)

    def decrypt(self, ciphertext: bytes) -> bytes:
        """decrypt
        Decrypt a piece of ciphertext.
        :param ciphertext: Base64 encoded ciphertext to decrypt.
        :type ciphertext: bytes
        :rtype: bytes
        """
        decoded_ciphertext = base64.b64decode(ciphertext)
        padded_plaintext = self.cipher.decrypt(decoded_ciphertext)
        try:
            plaintext = Padding.unpad(padded_plaintext,block_size=self.BLOCK_SIZE)
            logger.debug("AES verified successfully!")
            return plaintext
        except ValueError:
            logger.error(
                "AES could not be verfied."
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
        ciphertext = self.cipher.encrypt(Padding.pad(data,block_size=self.BLOCK_SIZE))
        return base64.b64encode(ciphertext)