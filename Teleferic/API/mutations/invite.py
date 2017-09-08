import graphene

import json

from .common_types import MessageEnvelope 

from API.Mock import execute_invite, execute_authorize

class InvitationMessage(graphene.InputObjectType):
  content = graphene.String(description="b58(encrypt(passphrase))")
  key = graphene.String(description="b58(passphrase(privkey))")

class Invite(graphene.Mutation):
    class Input():
      envelope = MessageEnvelope()
      message = InvitationMessage()

    ok = graphene.Boolean(required=True)
    message = graphene.String()
    id = graphene.String()

    @staticmethod
    def mutate(root, args, context, info):
      envelope = args.get('envelope')
      sender = envelope.get('sender')
      sender_sign = envelope.get('sign')

      message = args.get('message')
      message_content = message.get('content')
      message_key = message.get('key')
      message_dump = json.dumps(args.get('message'))
      
      result_authorize = execute_authorize(sender,message_dump,sender_sign)

      if(result_authorize.get('success') == False):
        return Invite(ok = False,message=result_authorize.get('message'))

      result = execute_invite(message_content,message_key,sender)
      
      return Invite(
        ok=True,
        id=result
      )

class Mutation(graphene.AbstractType):
    invite = Invite.Field()