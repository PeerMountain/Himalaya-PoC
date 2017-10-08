import graphene

from .sh256 import SHA256
from .address import Address
from.encrypted_content import AESEncryptedContent

class InvitationAbstract(graphene.AbstractType):
    bootstrapNode = graphene.String(required=True)
    bootstrapAddr = Address()
    offeringAddr = Address()
    serviceAnnouncementMessage = SHA256()
    serviceOfferingID = graphene.Int()
    inviteName = AESEncryptedContent()

class Invitation(graphene.InputObjectType, InvitationAbstract):
  '''
  Message Envelope
  Registred Sender and valid Signature
  '''
  pass