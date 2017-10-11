import graphene

from ..types import Address, RSAKey, Sign
from ..Mock import Reader, Authorize

class SignedTimestamp(graphene.ObjectType):
  timestamp = graphene.Float()
  signature = Sign()

class Teleferic(graphene.ObjectType):
  address = Address()
  pubkey = RSAKey()
  nickname = graphene.String()

  def resolve_pubkey(self, *args):
    return Reader.get_pubkey(self.address)
  
  def resolve_nickname(self, *args):
    return Reader.get_nickname(self.address)
    
class Query(graphene.AbstractType):
  teleferic = graphene.Field(Teleferic,
    description='''
    Retrive information
    from Teleferic
    like nickname or address
    and signed-timestamp.
    '''
  )

  def resolve_teleferic(self, *args):
    return Teleferic(
      address= Reader.get_address('Teleferic')
    )

  timestamp = graphene.Field(SignedTimestamp)
  def resolve_timestamp(self, *args):
    return SignedTimestamp(*Authorize.sign_current_timestamp())