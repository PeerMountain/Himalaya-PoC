import base58
import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signer
from Crypto.Hash import RIPEMD

from . import Reader
import time
import os

def authorize_message(envelope):
  sender = envelope.get('sender')
  ACL = envelope.get('ACL')
  pubkey = Reader.get_pubkey(sender)
  sign = envelope.get('messageSig')
  message_hash = envelope.get('messageHash')
  content= envelope.get('message')
  if ACL:
    for ACL_rule in ACL:
      # Rise an exception if some address be not registred
      Reader.get_pubkey(sender)
  pubkey_decoded = base58.b58decode(pubkey)
  key = RSA.importKey(pubkey_decoded)
  signer = Signer.new(key)
  content_hash = RIPEMD.new(content)
  if message_hash != content_hash.digest():
    raise Exception("Invalid hash")
  
  sign_decode = base58.b58decode(sign)
  result = signer.verify(content_hash,sign_decode)
  if result == False:
    raise Exception("Invalid sign")
  
  return True

def sign_current_timestamp():
  base_path = os.path.dirname(os.path.abspath(__file__))
  identity_filepath = os.path.join(base_path,'teleferic.priv')
  privkey_file = open(identity_filepath, 'rb')
  key = RSA.importKey(privkey_file.read())
  signer = Signer.new(key)
  
  timestamp = str(time.time())
  signature = base64.b64encode(signer.sign(RIPEMD.new(timestamp))).decode('utf-8')
  
  return [timestamp,signature]