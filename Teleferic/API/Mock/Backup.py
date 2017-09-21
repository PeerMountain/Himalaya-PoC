import base58
from Crypto.Hash import RIPEMD, SHA256
from Crypto.PublicKey import RSA
from API.models import Backup
import os

CONTAINER_PREFIX = [1, 0]
CONTAINER_STORAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)),'containers')

def get_container_hash(content):
    #The content is hashed SHA-256.
    step_1 = SHA256.new(content.encode('utf8')).digest()
    #The resulting Hash is further hashed with RIPEMD-160.
    step_2 = RIPEMD.new(step_1).digest()
    #Two bytes are prefixed to the resulting RIPEMD-160 hash in order to identify the deployment system.
    step_3 = bytes(CONTAINER_PREFIX)+step_2
    #A checksum is calculated by SHA-256 hashing the extended RIPEMD-160 hash, then hashing
    #the resulting hash once more.
    step_4_checksum = SHA256.new(SHA256.new(step_3).digest()).digest()
    #The last 4 bytes of the final hash are added as the 
    #trailing 4 bytes of the extended RIPEMD-160 hash. This is the checksum
    step_4 = step_3 + step_4_checksum[4:]
    #The resulting object is Base58 encoded
    return base58.b58encode(step_4)

def execute_backup(description,content,key,sender):
  container_hash = get_container_hash(content)
  container_path = os.path.join(CONTAINER_STORAGE,container_hash)

  file = open(container_path, 'w+')
  file.write(content)
  backup = Backup(
    description=description,
    hash=container_hash,
    key=key,
    sender=sender
  )
  backup.save()
  return container_hash