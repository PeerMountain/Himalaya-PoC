import graphene

class BaseAbstract(graphene.AbstractType):
  sender = graphene.String(description="Sender Address", required=True)
  pubkey = graphene.String(description="Sender PubKey")
  sign = graphene.String(description="Sender Sign", required=True)
  

class MessageEnvelope(graphene.InputObjectType, BaseAbstract):
  '''
  Message Envelope
  '''
  pass