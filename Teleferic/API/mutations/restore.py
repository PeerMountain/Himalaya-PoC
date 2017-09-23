import graphene

import json

from .common_types import MessageEnvelope 

from API.Mock import execute_restore, execute_restore_container, execute_authorize

from graphql import GraphQLError

class RestoreMessage(graphene.InputObjectType):
  hash = graphene.String(description="Backup Hash")
  sender = graphene.String(description="Backup Sender")

class RestoreResponse(graphene.ObjectType):
  description = graphene.String(description="Backup Description")
  key = graphene.String(description="Backup Key")
  sender = graphene.String(description="Backup Sender")
  hash = graphene.String(description="Backup Hash")
  content = graphene.String(description="Backup Content")

  def resolve_content(self, *args):
    return execute_restore_container(self.hash)

class Restore(graphene.Mutation):
    class Input():
      envelope = MessageEnvelope()
      message = RestoreMessage()

    ok = graphene.Boolean(required=True)
    restore_container = graphene.Field(lambda: RestoreResponse)

    @staticmethod
    def mutate(root, args, context, info):
      envelope = args.get('envelope')
      sender = envelope.get('sender')
      sender_sign = context.POST.get('sign')
      content = context.POST.get('query')+context.POST.get('variables')
      
      try:
        execute_authorize(sender,content,sender_sign)
      except Exception as e:
        return Restore(ok=False)
      
      message = args.get('message')
      message_hash = message.get('hash')
      message_sender = message.get('sender')
      
      try:
        result = execute_restore(message_sender,message_hash)
      except Exception as e:
        return Restore(ok=False)

      return Restore(
        ok=True,
        restore_container=RestoreResponse(**result)
      )

class Mutation(graphene.AbstractType):
    restore = Restore.Field()