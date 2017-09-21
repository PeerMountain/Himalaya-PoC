import graphene

import json

from .common_types import ThirdPersonMessageEnvelope 

from API.Mock import execute_register, execute_verify

class RegistrationMessage(graphene.InputObjectType):
  token = graphene.String(description="Invitation Token")

class Register(graphene.Mutation):
    class Input():
      envelope = ThirdPersonMessageEnvelope()
      message = RegistrationMessage()

    ok = graphene.Boolean()
    message = graphene.String()

    @staticmethod
    def mutate(root, args, context, info):
      envelope = args.get('envelope')
      sender_pubkey = envelope.get('pubkey')
      sender_sign = context.POST.get('sign')
      content = context.POST.get('query')+context.POST.get('variables')
      result_authorize = execute_verify(sender_pubkey,content,sender_sign)

      if(result_authorize.get('success') == False):
        return Register(ok=False,message=None)

      sender = envelope.get('sender')
      message = args.get('message')
      token = message.get('token')
      

      result = execute_register(token,sender,sender_pubkey)
      
      if(result == False):
        return Register(ok = False, message='Result')
      
      return Register(ok=True)

class Mutation(graphene.AbstractType):
    register = Register.Field()