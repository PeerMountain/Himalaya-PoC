import graphene

from API.mutations import send_message_mutation

from API.query import persona_query, teleferic_query

class Mutations(
        send_message_mutation,
        graphene.ObjectType
    ):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Query(
        persona_query,
        teleferic_query,
        graphene.ObjectType
    ):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query,mutation=Mutations)