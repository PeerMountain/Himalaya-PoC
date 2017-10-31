# -- FILE: features/steps/register.py
import os
from behave import given, when, then, step

from Crypto.PublicKey import RSA as Key
from Crypto.Hash import HMAC, SHA256
from libs.tools import RSA, AES, Identity

import json

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
  context.personaName = persona_name

@given('service info of "{service_name}"')
def step_imp(context, service_name):
  context.service = SERVICE_MAP.get(service_name)

@given('valid genesis invitation message')
def step_imp(context):
  cipher = AES(context.inviteKey)
  encrypted_invite_name = cipher.encrypt(context.inviteName).decode()

  message_body_partial = {
    'inviteName': encrypted_invite_name
  }
  message_body = json.dumps({**message_body_partial,**context.service})
  body_hash = SHA256.new(message_body.encode())

  dossier_hash = HMAC.new(context.dossierSalt.encode(),message_body.encode(),SHA256)
  message_content_raw = json.dumps({
    "dossierSalt": context.dossierSalt,
    "bodyType": 0,
    "messageBody": message_body
  })

  message_content = AES('Peer Mountain').encrypt(message_content_raw).decode()

  genesis_identity = Identity(context.REGISTRED_IDENTITY)

  message_sign = genesis_identity.sign(message_content.encode()).decode()

  context.message_hash = SHA256.new(message_content.encode())

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
    "messageHash": context.message_hash.hexdigest(), 
    "dossierHash": dossier_hash.hexdigest(),
    "bodyHash": body_hash.hexdigest(),
    "messageSig": message_sign,
    "message": message_content,
  }
  executed = context.client.execute(query,variable_values=variables)

  assert executed.get('errors') == None
  assert {
    "data": {
      "sendMessage": {
        "messageHash": context.message_hash.hexdigest()
      }
    }
  } == executed

@when('I compose valid registration message to {service_name}')
def step_imp(context, service_name):
  context.execute_steps('''
      When I query the pubkey of Teleferic
  ''')
  telefericPubkey = Key.importKey(context.executed['data']['teleferic']['persona']['pubkey'])
  teleferic_key = RSA(telefericPubkey)
  
  context.service = SERVICE_MAP.get(service_name)


  invite_name = teleferic_key.encrypt(context.inviteName.encode())
  key_proof = teleferic_key.encrypt(context.inviteKey.encode())
  
  message_body = json.dumps({
    'inviteMsgID': context.message_hash.hexdigest(),
    'keyProof': key_proof,
    'inviteName': invite_name,
    'publicKey': context.identity.pubkey.decode(),
    'publicNickname' : context.personaName
  })

  body_hash = SHA256.new(message_body.encode())

  dossier_hash = HMAC.new(context.dossierSalt.encode(),message_body.encode(),SHA256)
  message_content_raw = json.dumps({
    "dossierSalt": context.dossierSalt,
    "bodyType": 1,
    "messageBody": message_body
  })

  message_content = AES('Peer Mountain').encrypt(message_content_raw).decode()

  message_sign = context.identity.sign(message_content.encode()).decode()

  context.message_hash = SHA256.new(message_content.encode())

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
    "messageHash": context.message_hash.hexdigest(), 
    "dossierHash": dossier_hash.hexdigest(),
    "bodyHash": body_hash.hexdigest(),
    "messageSig": message_sign,
    "message": message_content,
  }

@when('I change {attribute} with {value}')
def step_imp(context,attribute,value):
  context.__setattr__(attribute,value)

@when('I send registration message')
def step_imp(context):
  context.executed = context.client.execute(context.query,variable_values=context.variables)

@then('response should be {result}')
def step_imp(context,result):
  if result == 'success':
    assert context.executed.get('errors') == None
    assert {
      "data": {
        "sendMessage": {
          "messageHash": context.message_hash.hexdigest()
        }
      }
    } == context.executed
  else:
    assert context.executed.get('errors') != None
