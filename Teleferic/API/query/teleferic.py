import graphene

from ..types import Address, RSAKey, Sign
from ..Mock import Reader, Teleferic_Identity

from .persona import Persona
from settings import VERSION_NAME, VERSION_CODE, BUILD_NUMBER

class Version(graphene.ObjectType):
    name = graphene.String()
    code = graphene.String()
    build_number = graphene.Int()

    def resolve_name(self, *args):
        return VERSION_NAME
    
    def resolve_code(self, *args):
        return VERSION_CODE

    def resolve_build_number(self, *args):
        return BUILD_NUMBER
  

class Teleferic(graphene.ObjectType):
  '''
  Teleferic type
  '''
  persona = graphene.Field(Persona,description='''
  Teleferic persona info
  ''')
  def resolve_persona(self,*args):
    teleferic_identity = Reader.get_persona(nickname='Teleferic')
    return Persona(
      nickname=teleferic_identity.nickname,
      address=teleferic_identity.address,
      pubkey=teleferic_identity.pubkey.encode()
    )

  signedTimestamp = graphene.Field(Sign,description='''
  Teleferic's timestamp singned by Teleferic itself
  ''')
  def resolve_signedTimestamp(self, info, **args):
    return Teleferic_Identity.sign_current_timestamp()

  version = graphene.Field(Version,description='''
  Teleferic current version
  ''')
  def resolve_version(self, info, **args):
      return Version()

class Query():
  teleferic = graphene.Field(Teleferic,
    description='''
    Retrive information
    from Teleferic
    like nickname or address
    and signed-timestamp.
    '''
  )

  def resolve_teleferic(self, info, **args):
    return Teleferic()