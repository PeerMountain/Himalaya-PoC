import base58
from Crypto.Hash import RIPEMD, SHA256
from Crypto.PublicKey import RSA
from API.models import Persona
import os

CONTAINER_STORAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)),'containers')

def get_pubkey(address):
  persona = Persona.objects.get(address=address)
  if not persona:
    raise Exception('Invalid address')
  return persona.pubkey

def get_nickname(address):
  persona = Persona.objects.get(pk=address)
  if not persona:
    raise Exception('Invalid address')
  return persona.nickname

def get_address(nickname):
  persona = Persona.objects.get(nickname=nickname)
  if not persona:
    raise Exception('Invalid nickname')
  return persona.address

def get_message_content(message_hash):
  container = open(os.path.join(CONTAINER_STORAGE,message_hash), 'r')
  content = container.read()
  return content