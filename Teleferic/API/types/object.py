import graphene

from .sha256 import SHA256
from .hmac_sha256 import HMACSHA256
from .sign import Sign
from .blob import AESEncryptedBlob, RSAEncryptedBlob

class ContainerAbstract():
  containerHash = SHA256(required=True)
  containerSign = Sign(required=True)
  objectContainer = AESEncryptedBlob(required=True)

class ContainerInput(graphene.InputObjectType, ContainerAbstract):
  pass

class ObjectAbstract():
  objectHash = SHA256(required=True)
  metaHashes = graphene.List(HMACSHA256, required=True)

class ObjectInput(graphene.InputObjectType, ObjectAbstract):
  container = ContainerInput()
  pass
