import base58
from Crypto.Hash import RIPEMD, SHA256
from Crypto.PublicKey import RSA
from API.models import Message, Persona, ACLRule
from . import Reader 
from libs.tools import Identity
import time
import os

MESSAGES_STORAGE = os.path.join(os.path.dirname(os.path.abspath(__file__)),'messages')

def add_persona(pubkey,nickname):
  identity = Identity(pubkey)

  persona = Persona(
    address= identity.address,
    pubkey= identity.pubkey,
    nickname= nickname
  )

  persona.save()

  return persona

def write_message(envelope):
  content= envelope.get('message')
  acl_rules= []

  acl = envelope.get('ACL')
  if not acl == None:
    for acl_rule in envelope.get('ACL'):
      acl_rule['reader'] = Persona.objects.get(pk=acl_rule.get('reader'))
      if not acl_rule['reader']:
        raise Exception('Invalid reader address')  
      acl_rules.append(ACLRule.objects.create(**acl_rule))

  message = Message(
    messageHash= envelope.get('messageHash'),
    messageType= envelope.get('messageType'),
    dossierHash= envelope.get('dossierHash'),
    bodyHash= envelope.get('bodyHash'),
    sender= Persona.objects.get(pk=envelope.get('sender')),
  )

  for acl_rule in acl_rules:
    message.acl.add(acl_rule)
  
  message.save()

  container_path = os.path.join(MESSAGES_STORAGE,message.messageHash)
  file = open(container_path, 'w+')
  file.write(content)

  return {
    "envelopeID": message.pk,
    "cacheTXID": message.pk,
    "cacheTimestamp": time.time(),
    "messageHash": message.messageHash
  }