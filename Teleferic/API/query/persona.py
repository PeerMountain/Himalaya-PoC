import graphene

from ..types import Address, RSAKey, Persona
from graphene_django.types import DjangoObjectType
from ..Mock import Reader

class Query():
  persona = graphene.Field(Persona,
    address=Address(default_value=None),
    nickname=graphene.String(default_value='Teleferic'),
    pubkey=graphene.String(default_value=None),
    description='''
    Retrive identity info
    filtering by 
    nickname, address or pubkey.
    '''
  )

  def resolve_persona(self, info, **args):
    persona= Reader.get_persona(
      args.get('address'),
      args.get('nickname'),
      args.get('pubkey')
    )
    return Persona(
      address=persona.address,
      nickname=persona.nickname,
      pubkey=persona.pubkey.encode()
    )
