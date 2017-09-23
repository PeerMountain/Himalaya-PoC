import base58
from Crypto.Hash import RIPEMD, SHA256
from Crypto.PublicKey import RSA
from API.models import Backup
import os

CONTAINER_STORAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)),'containers')

def execute_restore(sender=None,hash=None):
  if not sender is None:
    backup = Backup.objects.get(sender=sender)
  if not hash is None:
    backup = Backup.objects.get(hash=hash)
  
  if not backup:
    raise Exception("Backup not exist")

  return {
    'description':backup.description,
    'key': backup.key,
    'sender': backup.sender,
    'hash': backup.hash
  }

def execute_restore_container(hash):
  container = open(os.path.join(CONTAINER_STORAGE,hash), 'r')
  content = container.read()
  return content