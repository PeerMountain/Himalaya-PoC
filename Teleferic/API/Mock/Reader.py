import base58
from Crypto.Hash import RIPEMD, SHA256
from Crypto.PublicKey import RSA
from API.models import Persona
from libs.tools import Identity
import os

MESSAGES_STORAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)),'messages')

def get_persona(address=None, nickname=None, pubkey=None):
  
  if address != None:
    persona = Persona.objects.get(pk=address)
  elif nickname != None:
    persona = Persona.objects.get(nickname=nickname)
  elif pubkey != None:
    persona = Persona.objects.get(pubkey=pubkey)
  else:
    raise Exception('Define one filter')
  
  if not persona:
    raise Exception('Invalid filter')
  
  return persona

def check_persona_not_registred(pubkey,nickname):
  persona = Identity(pubkey)
  
  existent_identity = Persona.objects.filter(address=persona.address).first()
  if existent_identity is not None:
    raise Exception('Address already registred.')

  existent_identity = Persona.objects.filter(pubkey=persona.pubkey).first()
  if existent_identity is not None:
    raise Exception('Pubkey already registred.')

  existent_identity = Persona.objects.filter(nickname=nickname).first()
  if existent_identity is not None:
    raise Exception('Nickname already registred.')

  return True

def get_message_content(message_hash):
  container = open(os.path.join(MESSAGES_STORAGE,message_hash), 'r')
  content = container.read()
  return content