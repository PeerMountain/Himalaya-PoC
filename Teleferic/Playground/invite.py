from identity_tools import Identity
from Crypto.PublicKey import RSA
import random
import base58
import json
import os
from mingraphqlclient.min_graphql_clinet import MinGraphQLClient

from settings import IDENTITY_FOLDER, ENDPOINT

test_client= MinGraphQLClient(ENDPOINT)

identity_filename = input("Privkey name (identity): ")
identity_filepath= os.path.join(IDENTITY_FOLDER,identity_filename)

if identity_filename == '':
  identity_filepath = 'identity'
else:
  if os.path.isfile(identity_filepath) == False:
    print('File not exist')

privkey_file= open(identity_filepath, 'rb')
privkey= RSA.importKey(privkey_file.read())
identity= Identity(privkey)

passphrase = str(input("Passphrase (random): "))

if passphrase == '':
  passphrase = base58.b58encode(bytes(str(random.random()).encode('utf8')))
  print('Passphrase',passphrase)


invitation = identity.generate_invitation(passphrase=passphrase)

message_content = {
  'content': invitation.get('content'),
  'key': invitation.get('key')
}

sign = identity.sign(json.dumps(message_content))

query = '''
  mutation {
    invite(
      envelope: {
        sender: "'''+identity.address+'''"
        sign: "'''+sign+'''"
      }
      message: {
        content: "'''+invitation.get('content')+'''"
        key: "'''+invitation.get('key')+'''"
      }
    ) {
      ok
      id
      message
    }
  }
'''
print('Following query will execute:')
print (query)
response = json.loads(test_client.execute(query))
if False == response.get("data").get("invite").get("ok"):
  print('Error',response.get("data").get("invite").get("message"))
else:
  token = base58.b58encode(bytes(response.get("data").get("invite").get("id").encode('utf8'))+b'.'+bytes(base58.b58encode(bytes(passphrase.encode('utf8'))).encode('utf8')))
  print('Invitation token:', token)