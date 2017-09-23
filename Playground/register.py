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

parser = argparse.ArgumentParser(description='Generate register call')
parser.add_argument('-v', '--verbose', action='store_true', help='Prints query, variables and sign.')
args = parser.parse_args()

VERBOSE = args.verbose

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

query = '''
  mutation (
    $token: String!
    $sender: String!
    $pubkey: String!
  ){
    register(
      envelope: {
        sender: $sender
        pubkey: $pubkey
      }
      message: {
        token: $token
      }
    ){
      ok
    }
  }
'''

params_raw = {
  'token': token,
  'sender': identity.address,
  'pubkey': identity.pubkey
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

try:
  result = response.get("data").get("register").get("ok")
  if result == True:
    print('Registred success')
  else:
    print('Error',response_raw.text)
except:
  print('Error',response_raw.text)