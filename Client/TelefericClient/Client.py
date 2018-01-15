import requests
import json
import base64


class Client():

    def __init__(self, node='https://teleferic-dev.dxmarkets.com/teleferic/', debug=False):
        self.debug = debug
        self.node = node

    def request(self, query, variables=None):
        variables =  json.dumps(variables)
        r = requests.post(self.node, data={
            'query': query,
            'variables': variables
        })
        if self.debug:
            print('Query:\n%s' % query)
            print('variables:\n%s' % variables)
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
