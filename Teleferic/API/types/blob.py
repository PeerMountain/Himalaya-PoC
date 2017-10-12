from graphene.types import Scalar
from graphql.language import ast

class AESEncryptedBlob(Scalar):
    '''AES-256 encrypted content'''

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

class RSAEncryptedBlob(Scalar):
    '''RSA-4096 encrypted content'''

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