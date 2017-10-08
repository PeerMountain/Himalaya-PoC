import graphene

from .sh256 import SHA256
from .message_type import MessageType
from .address import Address
from .sign import Sign

from .acl_rule import ACLRule
from .container_hashes import ContainerHashesInput as ContainerHashes

class MessageEnvelopeAbstract(graphene.AbstractType):
    messageHash = SHA256()
    messageType = MessageType()
    messageSig= Sign()
    dossierHash = SHA256()
    bodyHash = SHA256()
    sender = Address()
    ACL = graphene.List(ACLRule)
    #containers = graphene.List(ContainerHashes)

class MessageEnvelope(graphene.InputObjectType, MessageEnvelopeAbstract):
  '''
  Message Envelope
  Registred Sender and valid Signature
  '''
  pass