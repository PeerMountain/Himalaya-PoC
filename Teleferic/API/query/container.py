import graphene

from API.types import Sign, HMACSHA256, MessageType, SHA256, Persona, AESEncryptedBlob, ACLRuleAbstract
from graphene_django.types import DjangoObjectType
from API.Mock import Reader
from API.Mock.utils import decode_hash, decode_dict


class ContainerOutput(graphene.ObjectType):
    containerHash = SHA256()
    objectHash = SHA256()
    objectContainer = AESEncryptedBlob()
    metaHashes = graphene.List(HMACSHA256)
    messages = graphene.List(SHA256)

    def __init__(self, data, *args, **kwargs):
        self.data = data

    def resolve_containerHash(self, info):
        return decode_hash(self.data.containerHash)

    def resolve_objectHash(self, info):
        return decode_hash(self.data.objectHash)

    def resolve_objectContainer(self, info):
        return Reader.get_container_content(decode_hash(self.data.containerHash))

    def resolve_saltedMetaHashes(self, info):
        saltedMetaHashes = []
        for saltedMetaHash in self.data.saltedMetaHashes.all():
            saltedMetaHashes.append(decode_hash(saltedMetaHash.saltedMetaHash))
        return saltedMetaHashes

    def resolve_messages(self, info):
      messages = self.data.messages.values_list('messageHash', flat=True)
      return [decode_hash(message) for message in messages]

class Query():
    container_by_hash = graphene.Field(ContainerOutput,
                             containerHash=SHA256(required=True))

    def resolve_container_by_hash(self, info, containerHash):
        container = Reader.get_container(containerHash)
        return ContainerOutput(container)
