import json
import requests


class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (bytes, bytearray)):
            return obj.decode('ASCII')
        return json.JSONEncoder.default(self, obj)


class GraphQLRequest():
    def __init__(self, node):
        self.node = node

    def send(self, query, variables):
        variables = json.dumps(variables, cls=JsonEncoder)
        data = {
            'query': query,
            'variables': variables
        }

        request = requests.post(self.node, data)

        return request.json()
