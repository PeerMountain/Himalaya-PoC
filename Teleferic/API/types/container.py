import graphene

from .sha256 import SHA256
from .hmac_sha256 import HMACSHA256
from .sign import Sign
from .blob import AESEncryptedBlob, RSAEncryptedBlob

class ContainerAbstract():
  containerHash = SHA256()
  objectHash = SHA256()
  containerSig = Sign()
  objectContainer = AESEncryptedBlob()
  validUntil = RSAEncryptedBlob()
  retainUntil = RSAEncryptedBlob()
  saltedMetaHashes = graphene.List(HMACSHA256)

class ContainerInput(graphene.InputObjectType, ContainerAbstract):
  pass