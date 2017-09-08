import base58
from Crypto.PublicKey import RSA
from Crypto.Hash import RIPEMD

from .Register import execute_get_pubkey 

def execute_authorize(sender,content,sign):
  pubkey = execute_get_pubkey(sender)
  if pubkey == False:
    return {
      'success': False,
      'message': 'Invalid Sander'
    }
  pubkey_decoded = base58.b58decode(pubkey)
  key = RSA.importKey(pubkey_decoded)
  message_hash = RIPEMD.new(content).digest()
  sign_decode = (base58.b58decode_int(sign),)
  result = key.verify(message_hash,sign_decode)
  if result == True:
    return {
      'success': result
    }
  else:
    return {
      'success': False,
      'message': 'Invalid Sign'
      }

def execute_verify(pubkey,content,sign):
  try:
    pubkey_decoded = base58.b58decode(pubkey)
    key = RSA.importKey(pubkey_decoded)
    message_hash = RIPEMD.new(content).digest()
    sign_decode = (base58.b58decode_int(sign),)
    result = key.verify(message_hash,sign_decode)
    return {
      'success': True
    }
  except:
    pass
    return {
      'success': False,
      'message': 'Invalid Sign'
    }