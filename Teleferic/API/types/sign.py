from graphene.types import Scalar
from graphql.language import ast
import msgpack
import base64

class Sign(Scalar):
    '''RSA-4096 signature'''

    @staticmethod
    def serialize(value):
        return base64.b64encode(msgpack.packb(value)).decode()

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            #TODO: Make Verification
            return node.value

    @staticmethod
    def parse_value(value):
        return msgpack.unpackb(base64.b64decode(value))