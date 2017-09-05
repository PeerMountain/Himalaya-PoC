import base58
from Crypto.PublicKey import RSA
from Crypto.Hash import RIPEMD

def execute_authorize(pubkey,content,sign):
  try:
    pubkey_decoded = base58.b58decode(pubkey)
    key_pair = RSA.importKey(pubkey_decoded)
    hash = RIPEMD.new(content).digest()
    sign_decode = (base58.b58decode_int(sign),)
    result = key_pair.verify(hash,sign_decode)
    return result
  except:
    pass
    return False