import base58
from Crypto.Hash import RIPEMD, SHA256
from Crypto.PublicKey import RSA
from API.models import Persona
import os

CONTAINER_STORAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)),'containers')

def execute_get_pubkey(address):
  persona = Persona.objects.get(pk=address)
  if not persona:
    raise Exception('Invalid address')
  return persona.pubkey

def execute_get_message_content(message_hash):
  container = open(os.path.join(CONTAINER_STORAGE,message_hash), 'r')
  content = container.read()
  return content