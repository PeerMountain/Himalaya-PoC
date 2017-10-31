import graphene

import json

from ..Mock import Authorizer, Writer

from ..types import MessageEnvelope, TXID, SHA256

from graphql import GraphQLError

class Message(graphene.Mutation):
  class Input():
    envelope = MessageEnvelope(required=True)

  envelopeID = graphene.Int()
  cacheTXID = TXID()
  messageHash = SHA256()
  cacheTimestamp = graphene.Float()

  @staticmethod
  def mutate(root, args, context, info):
    envelope = args.get('envelope')

    Authorizer.authorize_message(envelope)
    
    persisted = Writer.write_message(envelope)

    return Message(**persisted)

class Mutation(graphene.AbstractType):
  send_message = Message.Field(description='''
  Send PM message
  ''')