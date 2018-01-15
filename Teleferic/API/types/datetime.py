from graphene.types import Scalar
from graphql.language import ast
import datetime
import dateutil.parser

class DateTime(Scalar):
    '''Timedate in ISO fromat. Ej, 2018-01-16T17:14:39.019297+00:00'''

    @staticmethod
    def serialize(value):
        return value.isoformat()

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            #TODO: Make Verification
            return node.value

    @staticmethod
    def parse_value(value):
        return dateutil.parser.parse(value)