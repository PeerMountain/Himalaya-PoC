import base58
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as Signer
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
  signer = Signer.new(key)
  message_hash = RIPEMD.new(content)
  sign_decode = base58.b58decode(sign)
  result = signer.verify(message_hash,sign_decode)
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
    key = Signer.new(pubkey_decoded)
    signer = Signer.new(key)
    message_hash = RIPEMD.new(content)
    sign_decode = base58.b58decode(sign)
    result = signer.verify(message_hash,sign_decode)
    return {
      'success': True
    }
  except:
    pass
    return {
      'success': False,
      'message': 'Invalid Sign'
    }