from graphene.types import Scalar
from graphql.language import ast
import base64

class HMACSHA256(Scalar):
    '''HMAC-SHA-256 salted hash'''

    @staticmethod
    def serialize(value):
        return base64.b64encode(value).decode()

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            #TODO: Make Verification
            return node.value

    @staticmethod
    def parse_value(value):
        return base64.b64decode(value)