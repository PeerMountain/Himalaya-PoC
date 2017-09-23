import graphene

import json

from .common_types import MessageEnvelope 

from API.Mock import execute_invite, execute_authorize

from graphql import GraphQLError

class InvitationMessage(graphene.InputObjectType):
  content = graphene.String(description="b58(encrypt(passphrase))")
  key = graphene.String(description="b58(passphrase(privkey))")

class Invite(graphene.Mutation):
    class Input():
      envelope = MessageEnvelope()
      message = InvitationMessage()

    ok = graphene.Boolean(required=True)
    id = graphene.String()

    @staticmethod
    def mutate(root, args, context, info):
      envelope = args.get('envelope')
      sender = envelope.get('sender')
      sender_sign = context.POST.get('sign')
      content = context.POST.get('query')+context.POST.get('variables')

      try:
        execute_authorize(sender,content,sender_sign)
      except Exception as e:
        return Invite(ok=False)

      message = args.get('message')
      message_content = message.get('content')
      message_key = message.get('key')
      message_dump = json.dumps(args.get('message'))
      
      try:
        result = execute_invite(message_content,message_key,sender)
      except Exception as e:
        return Invite(ok=False)

      return Invite(
        ok=True,
        id=result
      )

class Mutation(graphene.AbstractType):
    invite = Invite.Field()