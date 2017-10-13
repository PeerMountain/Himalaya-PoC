import graphene

from .sh256 import SHA256
from .hmac_sha256 import HMACSHA256
from .message_type import MessageType
from .address import Address
from .sign import Sign

from .blob import AESEncryptedBlob, RSAEncryptedBlob

from .acl_rule import ACLRule
from .container_hashes import ContainerHashesInput as ContainerHashes

class MessageEnvelopeAbstract(graphene.AbstractType):
  sender = Address(description='''
  Sender PMAddress
  ''',required=True)
  messageType = MessageType(description='''
  Define general message type
  ''',required=True)
  messageHash = SHA256(description='''
  Contains SHA256 of encrypted message body
  ''',required=True)
  messageSig= Sign(description='''
  Contains messageHash siged with sender pubkey
  ''',required=True)
  dossierHash = HMACSHA256(description='''
  Contains HMAC-SHA256 of descrypted message usign dossierSalt as secret
  ''')
  bodyHash = SHA256(description='''
  Contains SHA256 of decrypted message body
  ''',required=True)
  message = AESEncryptedBlob(description='''
  AES Encrypted message
  ''',required=True)

class PrivateMessageEnvelope(graphene.InputObjectType, MessageEnvelopeAbstract):
  '''
  Private Message Envelope
  Registred Sender and valid Signature
  '''
  ACL = graphene.List(ACLRule,description='''
  Define a list of readers with encrypted keys
  ''',required=True)
  containers = graphene.List(ContainerHashes,description='''
  Contains hash of all containers present on message
  ''')

class PublicMessageEnvelope(graphene.InputObjectType, MessageEnvelopeAbstract):
  '''
  Public Message Envelope
  Valid Sender and valid Signature
  '''
  message = AESEncryptedBlob(description='''
  AES Encrypted message usign "Peer Mountain" as secret key
  ''',required=True)