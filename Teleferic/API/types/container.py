import graphene

from .sha256 import SHA256
from .hmac_sha256 import HMACSHA256
from .sign import Sign
from .blob import AESEncryptedBlob, RSAEncryptedBlob

class ContainerAbstract():
  containerHash = SHA256(required=True)
  objectHash = SHA256(required=True)
  containerSig = Sign()
  objectContainer = AESEncryptedBlob()
  saltedMetaHashes = graphene.List(HMACSHA256, required=True)

class ContainerInput(graphene.InputObjectType, ContainerAbstract):
  pass