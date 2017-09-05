import graphene

from settings import VERSION_NAME, VERSION_CODE, BUILD_NUMBER
from graphene_django.types import DjangoObjectType

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

class Query(graphene.AbstractType):
    version = graphene.Field(Version)

    def resolve_version(self, *args):
        return Version()
