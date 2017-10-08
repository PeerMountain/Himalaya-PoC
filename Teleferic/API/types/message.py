import graphene

from .message_envelope import MessageEnvelope
from .encrypted_content import AESEncryptedContent

class Message(graphene.AbstractType):
  envelope = MessageEnvelope()
  content = AESEncryptedContent()


class MessageInput(graphene.InputObjectType, Message):
  pass