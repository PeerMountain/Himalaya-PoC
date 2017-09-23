import graphene

import json

from .common_types import ThirdPersonMessageEnvelope 

from API.Mock import execute_register, execute_verify

from graphql import GraphQLError

class RegistrationMessage(graphene.InputObjectType):
  token = graphene.String(description="Invitation Token")

class Register(graphene.Mutation):
    class Input():
      envelope = ThirdPersonMessageEnvelope()
      message = RegistrationMessage()

    ok = graphene.Boolean(required=True)

    @staticmethod
    def mutate(root, args, context, info):
      envelope = args.get('envelope')
      sender_pubkey = envelope.get('pubkey')
      sender_sign = context.POST.get('sign')
      content = context.POST.get('query')+context.POST.get('variables')

      try:
        execute_verify(sender_pubkey,content,sender_sign)
      except Exception as e:
        return Register(ok=False)
      
      sender = envelope.get('sender')
      message = args.get('message')
      token = message.get('token')
      
      try:
        execute_register(token,sender,sender_pubkey)
      except Exception as e:
        return Register(ok=False)
      
      return Register(ok=True)

class Mutation(graphene.AbstractType):
    register = Register.Field()