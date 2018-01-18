import requests
import json
import base64
from pprint import pprint

class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (bytes, bytearray)):
            return obj.decode("ASCII")
        return json.JSONEncoder.default(self, obj)

class Client():

    def __init__(self, node='https://teleferic-dev.dxmarkets.com/teleferic/', debug=False):
        self.debug = debug
        self.node = node

    def request(self, query, variables=None):
        if self.debug:
            print('Query:\n%s' % query)
            print('variables:')
            pprint(variables)
            pprint(self.node)
        variables =  json.dumps(variables,  cls=JsonEncoder)
        if self.debug:
            print('variables encoded:')
            print(variables)
        r = requests.post(self.node, data={
            'query': query,
            'variables': variables
        })
        print(r.json())
        return r.json()

    def get_persona_pubkey(self, address):
        result = self.request('''
                query{
                    persona(
                        address: "%s"
                    ){
                        pubkey
                    }
                }
            ''' % address)
        return base64.b64decode(result['data']['persona']['pubkey'])

    def get_node_pubkey(self):
        result = self.request('''
                query{
                    teleferic{
                        persona{
                            pubkey
                        }
                    }
                }
            ''')
        return base64.b64decode(result['data']['teleferic']['persona']['pubkey'])

    def get_node_signedtimestamp(self):
        result = self.request('''
                query{
                    teleferic{
                        signedTimestamp
                    }
                }
            ''')
        return result['data']['teleferic']['signedTimestamp']
