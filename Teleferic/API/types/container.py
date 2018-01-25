import graphene

from .sha256 import SHA256
from .hmac_sha256 import HMACSHA256
from .sign import Sign
from .blob import AESEncryptedBlob, RSAEncryptedBlob

class ContainerAbstract():
  objectHash = SHA256(required=True)
  saltedMetaHashes = graphene.List(HMACSHA256, required=True)
  containerHash = SHA256()
  containerSig = Sign()
  objectContainer = AESEncryptedBlob()

class ContainerInput(graphene.InputObjectType, ContainerAbstract):
  pass