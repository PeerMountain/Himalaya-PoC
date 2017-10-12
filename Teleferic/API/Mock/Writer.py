import base58
from Crypto.Hash import RIPEMD, SHA256
from Crypto.PublicKey import RSA
from API.models import Message, Persona, ACLRule
import os

CONTAINER_PREFIX = [1, 0]
CONTAINER_STORAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)),'containers')

def write_message(envelope):
  content= envelope.get('message')
  acl_rules= []
  for acl_rule in envelope.get('ACL'):
    acl_rule['reader'] = Persona.objects.get(pk=acl_rule.get('reader'))
    if not acl_rule['reader']:
      raise Exception('Invalid reader address')  
    acl_rules.append(ACLRule.objects.create(**acl_rule))

  message = Message.objects.create(
    messageHash= envelope.get('messageHash'),
    messageType= envelope.get('messageType'),
    dossierHash= envelope.get('dossierHash'),
    bodyHash= envelope.get('bodyHash'),
    sender= envelope.get('sender'),
    ACL= acl_rules
  )

  container_path = os.path.join(CONTAINER_STORAGE,message.messageHash)
  file = open(container_path, 'w+')
  file.write(content)

  return message.messageHash