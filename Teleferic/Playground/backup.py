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

passphrase = str(input("Passphrase (random): "))

if passphrase == '':
  passphrase = base58.b58encode(bytes(str(random.random()).encode('utf8')))
  print('Passphrase',passphrase)


#Create Backup
rng = Random.new().read
backup_keypair = RSA.generate(4096, rng)

description = input("Backup description (string): ").encode('utf8')
content = input("Backup content (string): ").encode('utf8')

description_hash = RIPEMD.new(description)
content_hash = RIPEMD.new(content)

cipher = PKCS1_v1_5.new(backup_keypair)

backup_description = cipher.encrypt(bytes(description)+description_hash.digest())
backup_content = cipher.encrypt(bytes(content)+content_hash.digest())

backup_key = backup_keypair.exportKey('PEM',passphrase=passphrase,pkcs=8)

# Following query will execute
query = '''
  mutation (
    $sender: String!
    $description: String!
    $content: String!
    $key: String!
  ){
    backup(
      envelope: {
        sender: $sender
      }
      message: {
        description: $description
        content: $content
        key: $key
      }
    ) {
      ok
      hash
    }
  }
'''
#With this params 
params_raw = {
  'sender': identity.address,
  'description': base58.b58encode(backup_description),
  'content': base58.b58encode(backup_content),
  'key': base58.b58encode(backup_key)
}

params = json.dumps(params_raw)

graphql_query = {
  'query': query,
  'variables': params,
  'sign': identity.sign(query+params)
}

response_raw = requests.post(ENDPOINT, data = graphql_query)
response = response_raw.json()

try:
  print('Backup Hash:', response.get("data").get("backup").get("hash"))
except:
  print('Error', response_raw)