import graphene

import json

from ..Mock import Authorizer, Writer

from ..types import MessageEnvelope, TXID, SHA256

from graphql import GraphQLError

class Message(graphene.Mutation):
  class Arguments:
    envelope = MessageEnvelope(required=True)

  envelopeID = graphene.Int()
  cacheTXID = TXID()
  messageHash = SHA256()
  cacheTimestamp = graphene.Float()

  @staticmethod
  def mutate(root, info, **args):
    envelope = args.get('envelope')
    
    Authorizer.authorize_message(envelope)
    
    persisted = Writer.write_message(envelope)

    return Message(**persisted)

class Mutation():
  send_message = Message.Field(description='''
  Send PM message
  ''')