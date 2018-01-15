import graphene

from ..types import Address, RSAKey
from ..Mock import Reader

class Persona(graphene.ObjectType):
  address = Address()
  pubkey = RSAKey()
  nickname = graphene.String()