import requests
import json


class Client():

    def __init__(self, bootstrap_node='https://teleferic-dev.dxmarkets.com/teleferic/'):
        self.bootstrap_node = bootstrap_node

    def request(self, query, variables=None):
        print(variables)
        r = requests.post(self.bootstrap_node, data={
            'query': query,
            'variables': json.dumps(variables)
        })
        return r.json()
