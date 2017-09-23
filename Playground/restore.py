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

parser = argparse.ArgumentParser(description='Generate restore call')
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

print('Sender:', identity.address)

backup_hash = input('Backup hash: ')

if backup_hash == '':
  backup_hash = 'iYLvXswgGxfJXHFFj6i1gG6J6Vgwd6KfKLM7XyBc4jBnY6z7MVvbfnkwzavLKw3qXFR'

# Following query will execute
query = '''
  mutation (
    $sender: String!
    $hash: String!
  ){
    restore(
      envelope: {
        sender: $sender
      }
      message: {
        hash: $hash
      }
    ) {
      ok
      restoreContainer{
        key
        description
        content
      }
    }
  }
'''
#With this params 
params_raw = {
  'sender': identity.address,
  'hash': backup_hash
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


if response.get("data").get("restore").get("ok") == False:
  print('Error', response_raw.text)
  exit(1)

passphrase = str(input("Passphrase: "))

try:
  backup_key_raw = base58.b58decode(response.get("data").get("restore").get("restoreContainer").get("key"))
except:
  print('Error', response_raw.text)
  exit(1)
  
backup_key = RSA.importKey(backup_key_raw,passphrase=passphrase)

cipher = PKCS1_v1_5.new(backup_key)

dsize = RIPEMD.digest_size
sentinel = str(Random.new().read(15+dsize))

description_raw = response.get("data").get("restore").get("restoreContainer").get("description")
description_decode = base58.b58decode(description_raw)
description_digest = cipher.decrypt(description_decode, sentinel)
description = description_digest[:-dsize]
description_hash = description_digest[-dsize:]
description_digest = RIPEMD.new(description).digest()

if description_digest==description_hash:
  print('Backup Description:',description)

content_raw = response.get("data").get("restore").get("restoreContainer").get("content")
content_decode = base58.b58decode(content_raw)
content_digest = cipher.decrypt(content_decode, sentinel)
content = content_digest[:-dsize]
content_hash = content_digest[-dsize:]
content_digest = RIPEMD.new(content).digest()

if content_digest==content_hash:
  print('Backup Contet:',content)
