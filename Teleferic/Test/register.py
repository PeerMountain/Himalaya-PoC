from identity_tools import Identity
from Crypto.PublicKey import RSA
import base58
import json
import os

from mingraphqlclient.min_graphql_clinet import MinGraphQLClient

from settings import IDENTITY_FOLDER

graphql_endpoint = 'http://94.130.38.46/graphql'
graphql_endpoint = 'http://localhost/graphql'
test_client = MinGraphQLClient(graphql_endpoint)


token= input("Token: ")

identity_filename= input("Privkey Filename: ")
identity_filepath= os.path.join(IDENTITY_FOLDER,identity_filename)

if identity_filename == '':
  privkey_file= open('identity', 'rb')
  privkey= RSA.importKey(privkey_file.read())
  identity= Identity(privkey)
else:
  if os.path.isfile(identity_filepath) == True:
    print('File exist')
    exit(-1)

  identity = Identity()
  f = open(identity_filepath,'w')

  f.write(identity.key.exportKey('PEM').decode())
  f.close()

message_content = {
  'token': token
}

sign = identity.sign(json.dumps(message_content))

query = '''
  mutation {
    register(
      message: {
        token: "'''+token+'''"
      }
      
      envelope: {
        sender: "'''+identity.address+'''"
        pubkey: "'''+identity.pubkey+'''"
        sign: "'''+sign+'''"
      }
    ){
      ok
    }
  }
'''

print ( 'Following query will execute:' )
print ( query )
response = json.loads(test_client.execute(query))
if False == response.get("data").get("register").get("ok"):
  print('Error')
else:
  print('Registred success')