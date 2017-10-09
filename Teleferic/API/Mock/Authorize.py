import base58
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signer
from Crypto.Hash import RIPEMD

from . import Reader

def authorize(
  sender,
  content,
  content_hash,
  sign,
  ACL=None):
  pubkey = Reader.get_pubkey(sender)
  if ACL:
    for ACL_rule in ACL:
      # Rise an exception if some address be not registred
      Reader.get_pubkey(sender)
  pubkey_decoded = base58.b58decode(pubkey)
  key = RSA.importKey(pubkey_decoded)
  signer = Signer.new(key)
  message_hash = RIPEMD.new(content)
  if content_hash != message_hash.digest():
    raise Exception("Invalid hash")
  
  sign_decode = base58.b58decode(sign)
  result = signer.verify(message_hash,sign_decode)
  if result == False:
    raise Exception("Invalid sign")
  
  return True