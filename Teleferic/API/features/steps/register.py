# -- FILE: features/steps/register.py
import os
from behave import given, when, then, step

from Crypto.PublicKey import RSA as Key
from Crypto.Hash import HMAC, SHA256
from libs.tools import RSA, AES, Identity

import base64
import msgpack
import json

from collections import OrderedDict

IDENTITY_MAP = {}

SERVICE_MAP = {
  'service_1': {
    'bootstrapNode': 1,
    'bootstrapAddr': 1,
    'offeringAddr': 1,
    'serviceAnnouncementMessage': 1,
    'serviceOfferingID': 1,
  }
}

@given('{persona_name} identity')
def step_imp(context, persona_name):
  identity = IDENTITY_MAP.get(persona_name)
  if identity is None:
    new_identity = Identity()
    IDENTITY_MAP[persona_name] = new_identity
    identity = new_identity
  context.identity = identity
  context.personaName = persona_name.strip().encode()

@given('service info of "{service_name}"')
def step_imp(context, service_name):
  context.service = SERVICE_MAP.get(service_name)

@given('valid genesis invitation message')
def step_imp(context):
  cipher = AES(context.inviteKey)
  encrypted_invite_name = cipher.encrypt(context.inviteName)

  message_body_partial = {
    'inviteName': encrypted_invite_name
  }
  message_body = base64.b64encode(msgpack.packb({**message_body_partial,**context.service}))
  body_hash = SHA256.new(message_body)

  dossier_hash = HMAC.new(context.dossierSalt,message_body,SHA256)
  message_content_raw = msgpack.packb({
    "dossierSalt": context.dossierSalt,
    "bodyType": 0,
    "messageBody": message_body
  })

  message_content = AES(b'Peer Mountain').encrypt(message_content_raw)

  genesis_identity = Identity(context.REGISTRED_IDENTITY)

  executed = context.client.execute('''
    query{
      teleferic{
        signedTimestamp
      }
    }
  ''')
  assert not 'errors' in executed

  signable_object = OrderedDict()
  signable_object['messageHash'] = base64.b64encode(SHA256.new(message_content).digest())
  signable_object['timestamp'] = executed['data']['teleferic']['signedTimestamp']

  signable_object_format = msgpack.packb(signable_object)

  signature = genesis_identity.sign(signable_object_format)

  message_sign = base64.b64encode(msgpack.packb({
    "signature": signature,
    "timestamp": executed['data']['teleferic']['signedTimestamp']
  }))

  context.message_hash = SHA256.new(message_content)

  query = '''
    mutation (
      $sender: Address!
      $messageType: MessageType!
      $messageHash: SHA256!
      $bodyHash: SHA256!
      $messageSig: Sign!
      $message: AESEncryptedBlob!
      $dossierHash: HMACSHA256!
    ){
      sendMessage(
        envelope: {
          sender: $sender
          messageType: $messageType
          messageHash: $messageHash
          bodyHash: $bodyHash
          messageSig: $messageSig
          message: $message
          dossierHash: $dossierHash
        }
      ) {
        messageHash
      }
    }
  '''

  variables = {
    "sender": genesis_identity.address,
    "messageType": 'REGISTRATION',
    "messageHash":base64.b64encode(context.message_hash.digest()).decode(), 
    "dossierHash": base64.b64encode(dossier_hash.digest()).decode(),
    "bodyHash": base64.b64encode(body_hash.digest()).decode(),
    "messageSig": message_sign.decode(),
    "message": message_content.decode(),
  }
  executed = context.client.execute(query,variable_values=variables)

  assert executed.get('errors') == None
  assert {
    "data": {
      "sendMessage": {
        "messageHash": base64.b64encode(context.message_hash.digest()).decode()
      }
    }
  } == executed

@when('I compose valid registration message to {service_name}')
def step_imp(context, service_name):
  context.execute_steps('''
      When I query the pubkey of Teleferic
  ''')
  telefericPubkey = Key.importKey(base64.b64decode(context.executed['data']['teleferic']['persona']['pubkey']))
  teleferic_key = RSA(telefericPubkey)

  context.service = SERVICE_MAP.get(service_name)

  invite_name = teleferic_key.encrypt(context.inviteName)
  key_proof = teleferic_key.encrypt(context.inviteKey)
  
  message_body = base64.b64encode(msgpack.packb({
    'inviteMsgID': base64.b64encode(context.message_hash.digest()).decode(),
    'keyProof': key_proof.decode(),
    'inviteName': invite_name.decode(),
    'publicKey': context.identity.pubkey.decode(),
    'publicNickname' : context.personaName.decode()
  }))

  body_hash = SHA256.new(message_body)

  dossier_hash = HMAC.new(context.dossierSalt,message_body,SHA256)
  message_content_raw = msgpack.packb({
    "dossierSalt": context.dossierSalt,
    "bodyType": 1,
    "messageBody": message_body
  })

  message_content = AES(b'Peer Mountain').encrypt(message_content_raw)

  executed = context.client.execute('''
    query{
      teleferic{
        signedTimestamp
      }
    }
  ''')
  assert not 'errors' in executed

  signable_object = OrderedDict()
  signable_object['messageHash'] = base64.b64encode(SHA256.new(message_content).digest())
  signable_object['timestamp'] = executed['data']['teleferic']['signedTimestamp']

  signable_object_format = msgpack.packb(signable_object)

  signature = context.identity.sign(signable_object_format)

  message_sign = base64.b64encode(msgpack.packb({
    "signature": signature,
    "timestamp": executed['data']['teleferic']['signedTimestamp']
  }))

  context.message_hash = SHA256.new(message_content)

  context.query = '''
    mutation (
      $sender: Address!
      $messageType: MessageType!
      $messageHash: SHA256!
      $bodyHash: SHA256!
      $messageSig: Sign!
      $message: AESEncryptedBlob!
      $dossierHash: HMACSHA256!
    ){
      sendMessage(
        envelope: {
          sender: $sender
          messageType: $messageType
          messageHash: $messageHash
          bodyHash: $bodyHash
          messageSig: $messageSig
          message: $message
          dossierHash: $dossierHash
        }
      ) {
        messageHash
      }
    }
  '''

  context.variables = {
    "sender": context.identity.address,
    "messageType": 'REGISTRATION',
    "messageHash": base64.b64encode(context.message_hash.digest()).decode(), 
    "dossierHash": base64.b64encode(dossier_hash.digest()).decode(),
    "bodyHash": base64.b64encode(body_hash.digest()).decode(),
    "messageSig": message_sign.decode(),
    "message": message_content.decode(),
  }

@when('I change {attribute} with {value}')
def step_imp(context,attribute,value):
  context.__setattr__(attribute,value.strip().encode())

@when('I send registration message')
def step_imp(context):
  print(context.query)
  print(json.dumps(context.variables))
  context.executed = context.client.execute(context.query,variable_values=context.variables)

@then('response should be {result}')
def step_imp(context,result):
  if result == 'success':
    assert context.executed.get('errors') == None
    assert {
      "data": {
        "sendMessage": {
          "messageHash": base64.b64encode(context.message_hash.digest()).decode()
        }
      }
    } == context.executed
  else:
    assert context.executed.get('errors') != None
