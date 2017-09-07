import graphene

from API.mutations import register_mutation, invite_mutation

from API.query import version_query

class Mutations(
        register_mutation,
        invite_mutation,
        graphene.ObjectType
    ):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Query(
        version_query,
        graphene.ObjectType
    ):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query,mutation=Mutations)