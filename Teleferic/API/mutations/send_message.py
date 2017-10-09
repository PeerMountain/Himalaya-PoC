import graphene

import json

from ..Mock import Authorize, Writer

from ..types import MessageEnvelope, AESEncryptedContent

from graphql import GraphQLError

class Message(graphene.Mutation):
  class Input():
    envelope = MessageEnvelope()
    content = AESEncryptedContent()

  ok = graphene.Boolean(required=True)
  txid = graphene.String()

  @staticmethod
  def mutate(root, args, context, info):
    envelope = args.get('envelope')
    
    sender = envelope.get('sender')
    sender_sign = context.POST.get('sign')
    ACL = envelope.get('ACL')

    content = [context.POST.get('query'),context.POST.get('variables')]

    try:
      Authorize.authorize(sender,ACL,content,sender_sign)
    except Exception as e:
      return Message(ok=False)

    message = args.get('message')
    message_content = message.get('content')
    message_key = message.get('key')
    message_dump = json.dumps(args.get('message'))
    
    try:
      result = Writer.write_message(envelope,content)
    except Exception as e:
      return Message(ok=False)

    return Message(
      ok=True,
      txid=result
    )

class Mutation(graphene.AbstractType):
  send_message = Message.Field(description='''
  Send PM message
  ''')