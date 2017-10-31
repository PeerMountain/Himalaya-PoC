import graphene

from ..types import Address, RSAKey, Persona as PersonaAbstract
from graphene_django.types import DjangoObjectType
from ..Mock import Reader

class Persona(graphene.ObjectType, PersonaAbstract):
  pass
    
class Query(graphene.AbstractType):
  persona = graphene.Field(Persona,
    address=graphene.String(default_value=None),
    nickname=graphene.String(default_value='Teleferic'),
    pubkey=graphene.String(default_value=None),
    description='''
    Retrive identity info
    filtering by 
    nickname, address or pubkey.
    '''
  )

  def resolve_persona(self, info, *args):
    persona= Reader.get_persona(
      info.get('address'),
      info.get('nickname'),
      info.get('pubkey')
    )
    return Persona(
      address=persona.address,
      nickname=persona.nickname,
      pubkey=persona.pubkey
    )
