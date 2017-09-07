import graphene

import json

from .common_types import MessageEnvelope 

from API.Mock import execute_register, execute_verify

class RegistrationMessage(graphene.InputObjectType):
  token = graphene.String(description="Invitation Token")

class Register(graphene.Mutation):
    class Input():
      envelope = MessageEnvelope()
      message = RegistrationMessage()

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, args, context, info):
      envelope = args.get('envelope')
      message = args.get('message')
      token = message.get('token')
      sender = envelope.get('sender')
      sender_sign = envelope.get('sign')
      sender_pubkey = envelope.get('pubkey')
      message_dump = json.dumps(args.get('message'), ensure_ascii=False)

      result_verify = execute_verify(sender_pubkey,message_dump,sender_sign)

      if(result_verify.get('success') == False):
        return Register(ok = False)

      result = execute_register(token,sender,sender_pubkey)
      
      if(result == False):
        return Register(ok = False)
      
      return Register(ok=True)

class Mutation(graphene.AbstractType):
    register = Register.Field()