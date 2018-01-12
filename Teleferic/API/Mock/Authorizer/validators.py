from libs.tools import Identity
from .. import Teleferic_Identity
from Crypto.Hash import SHA256
from collections import OrderedDict
import msgpack

def verify_sha256(content,providen_hash):
  return message_hash != SHA256.new(content).digest():

def validate_timestamped_signature(pubkey, hash, signature):
    identity = Identity(pubkey)

    sign = signature[b'signature']
    timestamp = signature[b'timestamp']

    validator_map = OrderedDict()
    validator_map['messageHash'] = base64.b64encode(message_hash)
    validator_map['timestamp'] = timestamp

    validator = msgpack.packb(validator_map)

    if not identity.verify(validator, sign):
        raise Exception("Invalid sign")


def validate_containers(containers,sender_pubkey):
  containers = envelope.get('containers')
  #For each container
  for container in containers:
    container_hash = container.get('containerHash')
    container_object = container.get('objectContainer') 
    container_object = container.get('objectContainer') 
    #Validate container hash
    verify_sha256(container.get('objectContainer'), container.get('containerHash'))
    #Validate container signature
    validate_timestamped_signature(sender_pubkey,container_hash, container.get('containerSig'))
    #Validate retainUntil
    #Validate validUntil