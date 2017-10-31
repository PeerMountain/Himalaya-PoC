from Crypto.Cipher import PKCS1_v1_5 as Cipher
from Crypto.Signature import PKCS1_v1_5 as Signer
from Crypto.PublicKey import RSA as Key
from Crypto.PublicKey.RSA import _RSAobj
from Crypto.Hash import SHA256
from Crypto import Random

import base64

class RSA():
  def __init__(self, key):
    key_type = type(key)
    if key_type == str:
      self.key = Key.importKey(key)
    elif key_type == _RSAobj:
      self.key = key
    else:
      raise Exception('Invalid key format.')

  def encrypt(self, content):
    content_hash = SHA256.new(content)
    cipher = Cipher.new(self.key)
    return base64.urlsafe_b64encode(cipher.encrypt(content+content_hash.digest())).decode()

  def decrypt(self, cipher_content_raw):
    cipher_content = base64.urlsafe_b64decode(cipher_content_raw)

    dsize = SHA256.digest_size
    sentinel = Random.new().read(15+dsize)      # Let's assume that average data length is 15
    
    cipher = Cipher.new(self.key)
    message = cipher.decrypt(cipher_content, sentinel)

    digest = SHA256.new(message[:-dsize]).digest()
    if digest==message[-dsize:]:                # Note how we DO NOT look for the sentinel
      return message[:-dsize]
    else:
      raise Exception('Error in decryption')

  def sign(self, content):
    content_hash = SHA256.new(content)
    signer = Signer.new(self.key)
    return base64.urlsafe_b64encode(signer.sign(content_hash))

  def verify_sign(self, content, signature):
    sign = base64.urlsafe_b64decode(signature)
    content_hash = SHA256.new(content)
    verifier = Signer.new(self.key)
    return verifier.verify(content_hash, sign)