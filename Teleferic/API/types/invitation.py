import graphene

from .sh256 import SHA256
from .address import Address
from .blob import RSAEncryptedBlob

class InvitationAbstract(graphene.AbstractType):
    bootstrapNode = graphene.String(required=True)
    bootstrapAddr = Address()
    offeringAddr = Address()
    serviceAnnouncementMessage = SHA256()
    serviceOfferingID = graphene.Int()
    inviteName = RSAEncryptedBlob()

class Invitation(graphene.InputObjectType, InvitationAbstract):
  '''
  Message Envelope
  Registred Sender and valid Signature
  '''
  pass