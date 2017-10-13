import graphene

from ..types import Address, RSAKey
from graphene_django.types import DjangoObjectType
from ..Mock import Reader

class Persona(graphene.AbstractType):
  address = Address()
  pubkey = RSAKey()
  nickname = graphene.String()

  def resolve_pubkey(self, *args):
    return Reader.get_pubkey(self.address)
  
  def resolve_nickname(self, *args):
    return Reader.get_nickname(self.address)