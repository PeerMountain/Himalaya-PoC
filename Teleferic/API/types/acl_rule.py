import graphene

from .address import Address
from .key import AESKey

class ACLRuleAbstract(graphene.AbstractType):
  reader = Address()
  '''PM Address'''
  key = AESKey()
  '''Message key encrypted with reader public key'''

class ACLRule(graphene.InputObjectType, ACLRuleAbstract):
  pass