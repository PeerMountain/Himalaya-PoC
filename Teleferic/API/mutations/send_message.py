import graphene

import json

from ..Mock import Authorize, Writer

from ..types import PrivateMessageEnvelope

from graphql import GraphQLError

class PrivateMessage(graphene.Mutation):
  class Input():
    envelope = PrivateMessageEnvelope()

  ok = graphene.Boolean(required=True)
  txid = graphene.String()

  @staticmethod
  def mutate(root, args, context, info):
    envelope = args.get('envelope')

    try:
      Authorize.authorize_message(envelope)
    except Exception as e:
      return PrivateMessage(ok=False)
    
    try:
      result = Writer.write_message(envelope)
    except Exception as e:
      return PrivateMessage(ok=False)

    return PrivateMessage(
      ok=True,
      txid=result
    )

class Mutation(graphene.AbstractType):
  send_private_message = PrivateMessage.Field(description='''
  Send PM message
  ''')