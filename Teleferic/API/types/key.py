from graphene.types import Scalar
from graphql.language import ast
import base64

class AESKey(Scalar):
    '''40 bytes key encrypted with RSA-4096'''

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

class RSAKey(Scalar):
    '''RSA-4096 Pubkey'''

    @staticmethod
    def serialize(value):
        return base64.b64encode(value).decode('utf-8')

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            #TODO: Make Verification
            return node.value

    @staticmethod
    def parse_value(value):
        return base64.b64decode(value)