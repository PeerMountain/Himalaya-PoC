import graphene

class MessageType(graphene.Enum):
    SYSTEM = 0
    REGISTRATION = 1
    ASSERTION = 2
    ATTESTATION = 3
    SERVICE = 4
    DELEGATION = 5