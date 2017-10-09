import graphene

from ..types import Address, RSAKey
from graphene_django.types import DjangoObjectType
from ..Mock import Reader

class Persona(graphene.ObjectType):
  address = Address()
  pubkey = RSAKey()
  nickname = graphene.String()

  def resolve_pubkey(self, *args):
    return Reader.get_pubkey(self.address)
  
  def resolve_nickname(self, *args):
    return Reader.get_nickname(self.address)
    
class Query(graphene.AbstractType):
  persona = graphene.Field(Persona,
    address=graphene.String(default_value=None),
    nickname=graphene.String(default_value=None),
    description='''
    Retrive identity info
    filtering by 
    nickname or address.
    '''
  )

  def resolve_persona(self, info, *args):
    address= info.get('address')
    nickname= info.get('nickname')
    if not address:
      if nickname:
        return Persona(
          address= Reader.get_address(nickname)
        )
      else:
        raise Exception('Invalid nickname')
    elif nickname:
      raise Exception('Define only one filter argument.')
    return Persona(
      address= address
    )
