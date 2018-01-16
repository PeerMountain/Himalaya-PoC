import graphene

from API.types import Sign, HMACSHA256, MessageType, SHA256, Persona, AESEncryptedBlob, ACLRuleAbstract, ContainerAbstract
from graphene_django.types import DjangoObjectType
from API.Mock import Reader
from API.Mock.utils import decode_hash, decode_dict

class ACLRuleOutput(graphene.ObjectType, ACLRuleAbstract):
    reader = graphene.Field(Persona, description='''
    Sender PMAddress
    ''')

    def __init__(self, data, *args, **kwargs):
        self.data = data
        super(ACLRuleOutput, self).__init__(*args, **kwargs)

    
    def resolve_reader(self,info):
        return Persona(**{
            'address': self.data.reader.address,
            'pubkey': self.data.reader.pubkey.encode(),
            'nickname': self.data.reader.nickname
        })

    def resolve_key(self, info):
        return self.data.key


class ContainerOutput(graphene.ObjectType, ContainerAbstract):

    saltedMetaHashes = graphene.List(HMACSHA256)

    def __init__(self, data, *args, **kwargs):
        self.data = data
        super(ContainerOutput, self).__init__(*args, **kwargs)

    def resolve_containerHash(self, info):
        return decode_hash(self.data.containerHash)

    def resolve_objectHash(self, info):
        return decode_hash(self.data.objectHash)

    def resolve_containerSig(self, info):
        return decode_dict(self.data.containerSig)

    def resolve_objectContainer(self, info):
        return Reader.get_container_content(decode_hash(self.data.containerHash))

    def resolve_retainUntil(self, info):
        return self.data.retainUntil

    def resolve_validUntil(self, info):
        return self.data.validUntil

    def resolve_saltedMetaHashes(self, info):
        saltedMetaHashes = []
        for saltedMetaHash in self.data.saltedMetaHashes.all():
            saltedMetaHashes.append(decode_hash(saltedMetaHash.saltedMetaHash))
        return saltedMetaHashes


class MessageEnvelopeOutput(graphene.ObjectType):

    def __init__(self, data, *args, **kwargs):
        self.data = data
        super(MessageEnvelopeOutput, self).__init__(*args, **kwargs)

    sender = graphene.Field(Persona, description='''
    Sender PMAddress
    ''')
    messageHash = SHA256(description='''
    Contains SHA256 of encrypted message body
    ''')
    messageType = MessageType(description='''
    Define general message type
    ''')
    messageSig = Sign(description='''
    Contains messageHash siged with sender pubkey
    ''')
    dossierHash = HMACSHA256(description='''
    Contains HMAC-SHA256 of descrypted message usign dossierSalt as secret
    ''')
    bodyHash = SHA256(description='''
    Contains SHA256 of decrypted message body
    ''')
    ACL = graphene.List(ACLRuleOutput, description='''
    Define a list of readers with encrypted keys.
    If is empty, message will be public and content
    needs to be encrypted with 'Peer Mountain' passphrase
    ''')
    containers = graphene.List(ContainerOutput, description='''
    Contains hash of all containers present on message
    ''')
    message = AESEncryptedBlob(description='''
    AES Encrypted message
    ''')
    
    def resolve_sender(self, info):
        return Persona(**{
            'address': self.data.sender.address,
            'pubkey': self.data.sender.pubkey.encode(),
            'nickname': self.data.sender.nickname
        })
    
    def resolve_messageHash(self, info):
        return decode_hash(self.data.messageHash)

    def resolve_messageType(self, info):
        return self.data.messageType

    def resolve_messageSig(self,info):
        return decode_dict(self.data.messageSig)

    def resolve_dossierHash(self, info):
        return decode_hash(self.data.dossierHash)

    def resolve_bodyHash(self, info):
        return decode_hash(self.data.bodyHash)

    def resolve_ACL(self, info):
        acls = []
        for acl in self.data.acl.all():
            acls.append(ACLRuleOutput(acl))
        return acls

    def resolve_containers(self, info):
        containers = []
        for container in self.data.containers.all():
            containers.append(ContainerOutput(container))
        return containers

    def resolve_message(self, info):
        return Reader.get_message_content(decode_hash(self.data.messageHash))

class Query():
    message = graphene.Field(MessageEnvelopeOutput,
                             messageHash=SHA256(required=True))

    def resolve_message(self, info, messageHash):
        message = Reader.get_message(messageHash)
        return MessageEnvelopeOutput(message)
