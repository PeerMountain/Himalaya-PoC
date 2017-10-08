import graphene

from .sh256 import SHA256

class ContainerHashes(graphene.AbstractType):
  containerHash = SHA256()
  objectHash = SHA256()
  metahashes = graphene.List(SHA256)

class ContainerHashesInput(graphene.InputObjectType, ContainerHashes):
  pass