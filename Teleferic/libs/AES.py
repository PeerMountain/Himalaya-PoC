import base64
from Crypto import Random
from Crypto.Cipher import AES as Base_AES

class AES():

  bs=32

  def __init__(self, key):
    if(len(key) >= self.bs):
      raise Exception('Key length must be shorter or equal to {0}.'.format(self.bs-1))
    self.key = self.pad(key)

  
  def pad(self, s):
    return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

  def unpad(self, s):
    return s[:-ord(s[len(s) - 1:])]

  def encrypt(self, raw):
    raw = self.pad(raw)
    iv = Random.new().read(Base_AES.block_size)
    cipher = Base_AES.new(self.key, Base_AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))

  def decrypt(self, enc):
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = Base_AES.new(self.key, Base_AES.MODE_CBC, iv)
    return self.unpad(cipher.decrypt(enc[16:]))
