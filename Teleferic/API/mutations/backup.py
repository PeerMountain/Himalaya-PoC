import graphene

import json

from .common_types import MessageEnvelope 

from API.Mock import execute_backup, execute_authorize

class BackupMessage(graphene.InputObjectType):
  description = graphene.String(description="b58(encrypt(`some text or object with descriptions`))")
  content = graphene.String(description="b58(encrypt(content))")
  key = graphene.String(description="b58(passphrase(privkey))")

class Backup(graphene.Mutation):
    class Input():
      envelope = MessageEnvelope()
      message = BackupMessage()

    ok = graphene.Boolean(required=True)
    hash = graphene.String()

    @staticmethod
    def mutate(root, args, context, info):
      envelope = args.get('envelope')
      
      sender = envelope.get('sender')
      sender_sign = context.POST.get('sign')

      #args come on query or is mapped on variables
      content = context.POST.get('query')+context.POST.get('variables')
      
      result_authorize = execute_authorize(sender,content,sender_sign)

      message = args.get('message')
      message_description = message.get('description')
      message_content = message.get('content')
      message_key = message.get('key')


      if(result_authorize.get('success') == False):
        return Backup(ok = False,message=result_authorize.get('message'))

      result = execute_backup(message_description,message_content,message_key,sender)
      
      return Backup(
        ok=True,
        hash=result
      )

class Mutation(graphene.AbstractType):
    backup = Backup.Field()