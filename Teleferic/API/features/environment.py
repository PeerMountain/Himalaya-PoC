from django.core.management import call_command
from graphene.test import Client
from API.schema import schema

def before_feature(context, feature):
  call_command('loaddata', 'genesis_identity.json', verbosity=0)
  context.client = Client(schema)