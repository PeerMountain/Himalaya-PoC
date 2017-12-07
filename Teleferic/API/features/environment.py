from django.core.management import call_command
from graphene.test import Client
from Crypto.PublicKey import RSA
from API.schema import schema

def before_feature(context, feature):
  call_command('loaddata', 'genesis_identity.json', verbosity=0)
  context.client = Client(schema)
  context.REGISTRED_IDENTITY = RSA.importKey("""-----BEGIN RSA PRIVATE KEY-----
    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
    -----END RSA PRIVATE KEY-----""")