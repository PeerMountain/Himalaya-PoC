from graphene.types import Scalar
from graphql.language import ast

class HMACSHA256(Scalar):
    '''HMAC-SHA-256 salted hash'''

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