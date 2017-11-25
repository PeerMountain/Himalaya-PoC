import graphene

from .sh256 import SHA256
from .hmac_sha256 import HMACSHA256

class ContainerHashes():
  containerHash = SHA256()
  objectHash = SHA256()
  metaHashes = graphene.List(SHA256)
  saltedMetaHashes = graphene.List(HMACSHA256)

class ContainerHashesInput(graphene.InputObjectType, ContainerHashes):
  pass