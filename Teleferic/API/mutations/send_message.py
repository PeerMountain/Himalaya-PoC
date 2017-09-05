import graphene

from .common_types import MessageEnvelope

class SendMessage(graphene.Mutation):
    class Input:
        envelope = MessageEnvelope()
        bodyHash = graphene.String(required=False)
        dossierHash = graphene.String()
        reader = graphene.String()

    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, args, context, info):
        return SendMessage(ok=False)

class Mutation(graphene.AbstractType):
    send_message = SendMessage.Field(description="Aca!")