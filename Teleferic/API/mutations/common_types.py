import graphene

class BaseAbstract(graphene.AbstractType):
  sender = graphene.String(description="Sender Address", required=True)

class MessageEnvelope(graphene.InputObjectType, BaseAbstract):
  '''
  Message Envelope
  Registred Sender
  '''
  pass

class ThirdPersonMessageEnvelope(graphene.InputObjectType, BaseAbstract):
  '''
  Third Person Message Envelope
  Not registred Sender
  '''
  pubkey = graphene.String(description="Sender PubKey", required=True)