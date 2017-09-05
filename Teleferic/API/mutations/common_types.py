import graphene

class BaseAbstract(graphene.AbstractType):
  sender = graphene.String(description="Sender Address")
  pubkey = graphene.String(description="Sender PubKey")
  sign = graphene.String(description="Sender PubKey")
  

class MessageEnvelope(graphene.InputObjectType, BaseAbstract):
  '''
  Message Envelope
  '''
  pass