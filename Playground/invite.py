from Crypto.Hash import RIPEMD
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5

import random

import base58
import json

import os

from identity_tools import Identity
import requests

from settings import IDENTITY_FOLDER, ENDPOINT

import argparse

parser = argparse.ArgumentParser(description='Generate invite call')
parser.add_argument('-v', '--verbose', action='store_true', help='Prints query, variables and sign.')
args = parser.parse_args()

VERBOSE = args.verbose


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

query = '''
  mutation (
    $sender: String!
    $content: String!
    $key: String!
  ){
    invite (
      envelope: {
        sender: $sender
      }
      message: {
        content: $content
        key: $key
      }
    ) {
      ok
      id
    }
  }
'''
params_raw = {
  'sender': identity.address,
  'content': invitation.get('content'),
  'key': invitation.get('key')
}

params = json.dumps(params_raw)

graphql_query = {
  'query': query,
  'variables': params,
  'sign': identity.sign(query+params)
}

if VERBOSE:
  print(('/'*50)+' Begin Query '+('/'*50))
  print(graphql_query['query'])
  print(('/'*50)+' End Query '+('/'*50))
  print(('/'*50)+' Begin Variables '+('/'*50))
  print(graphql_query['variables'])
  print(('/'*50)+' End Variables '+('/'*50))
  print(('/'*50)+' Begin Sign '+('/'*50))
  print(graphql_query['sign'])
  print(('/'*50)+' End Sign '+('/'*50))

response_raw = requests.post(ENDPOINT, data = graphql_query)
response = response_raw.json()
invite_id = response.get("data").get("invite").get("id")

try:
  token = base58.b58encode(bytes(invite_id.encode('utf8'))+b'.'+bytes(base58.b58encode(bytes(passphrase.encode('utf8'))).encode('utf8')))
  print('Invitation token:', token)
except:
  print('Error',response_raw.text)