from graphene.types import Scalar
from graphql.language import ast

class SHA256(Scalar):
    '''SHA-256 hash'''

    @staticmethod
    def serialize(value):
        return value

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            #TODO: Make Verification
            return node.value

    @staticmethod
    def parse_value(value):
        return value