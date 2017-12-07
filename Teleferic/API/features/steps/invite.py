# -- FILE: features/steps/invite.py
import os
from behave import given, when, then, step

from Crypto.PublicKey import RSA as Key
from Crypto.Hash import HMAC, SHA256
from libs.tools import RSA, AES, Identity

from collections import OrderedDict

import json
import msgpack
import base64

@given('registred Identity stored in <identity>')
def step_impl(context):
  context.identity = Identity(context.REGISTRED_IDENTITY)

@given('Teleferic has pubkey <telefericPubkey>')
def step_impl(context):
  context.execute_steps('''
      When I query the pubkey of Teleferic
      And decode teleferic pubkey with Base64
  ''')
  context.telefericPubkey = Key.importKey(context.teleferic_pub)

@given('bootstrap url is "{bootstrapNode}"')
def step_impl(context,bootstrapNode):
  if bootstrapNode == 'None':
    context.bootstrapNode = None
  else:
    context.bootstrapNode = bootstrapNode.strip().encode()

@given('bootstrap PM-Address is "{bootstrapAddr}"')
def step_impl(context,bootstrapAddr):
  if bootstrapAddr == 'None':
    context.bootstrapAddr = None
  else:
    context.bootstrapAddr = bootstrapAddr.strip().encode()

@given('offering PM-Address is "{offeringAddr}"')
def step_impl(context, offeringAddr):
  if offeringAddr == 'None':
    context.offeringAddr = None
  else:
    context.offeringAddr = offeringAddr.strip().encode()

@given('service offering ID is "{serviceOfferingID}"')
def step_impl(context, serviceOfferingID):
  if serviceOfferingID == 'None':
    context.serviceOfferingID = None
  else:
    context.serviceOfferingID = serviceOfferingID.strip().encode()

@given('service announcement message is "{serviceAnnouncementMessage}"')
def step_impl(context,serviceAnnouncementMessage):
  if serviceAnnouncementMessage == 'None':
    context.serviceAnnouncementMessage = None
  else:
    context.serviceAnnouncementMessage = serviceAnnouncementMessage.strip().encode()

@given('invitation name is "{inviteName}"')
def step_impl(context,inviteName):
  if inviteName == 'None':
    context.inviteName = None
  else:
    context.inviteName = inviteName.strip().encode()

@given('invitation key is "{inviteKey}"')
def step_impl(context,inviteKey):
  if inviteKey == 'None':
    context.inviteKey = None
  else:
    context.inviteKey = inviteKey.strip().encode()

@given('dossier salt is "{dossierSalt}"')
def step_impl(context, dossierSalt):
  context.dossierSalt = dossierSalt.strip().encode()

@given('dossier hash is "{dossierHash}"')
def step_impl(context,dossierHash):
  context.dossierHash = dossierHash.strip().encode()

@given('message hash is "{messageHash}"')
def step_impl(context,messageHash):
  context.messageHash = messageHash.strip().encode()

@given('message sign is "{messageSign}"')
def step_impl(context,messageSign):
  context.messageSign = messageSign.strip().encode()

@given('body hash is "{bodyHash}"')
def step_impl(context,bodyHash):
  context.bodyHash = bodyHash.strip().encode()

@given('message type is "{messageType}", and is stored in <messageType>')
def step_impl(context, messageType):
  context.messageType = messageType.strip().encode()

@given('message body type is "{bodyType}", and is stored in <bodyType>')
def step_impl(context, bodyType):
  context.bodyType = int(bodyType.strip().encode())

@when('I encrypt "{inviteName}" using AES-256 with {inviteKey} and store it on <encryptedInviteName>')
def step_impl(context, inviteName, inviteKey):
  cipher = AES(context.inviteKey)
  context.encryptedInviteName = cipher.encrypt(context.inviteName)

@when('I compose invitation message with <encryptedInviteName>, {bootstrapNode}, {offeringAddr}, {serviceAnnouncementMessage}, {serviceOfferingID} and {inviteName}. And I store it in <messageBody>')
def step_impl(context, **args):
  context.messageBody = base64.b64encode(msgpack.packb({
    "bootstrapNode": context.bootstrapNode,
    "bootstrapAddr": context.bootstrapAddr,
    "offeringAddr": context.offeringAddr,
    "serviceAnnouncementMessage": context.serviceAnnouncementMessage,
    "serviceOfferingID": context.serviceOfferingID,
    "inviteName": context.encryptedInviteName
  }))

@when('I compose message content with {dossierSalt}, <bodyType> and <messageBody>. And I store it in <messageContent>')
def step_impl(context, **args):
  context.messageContent = msgpack.packb({
    "dossierSalt": context.dossierSalt,
    "bodyType": context.bodyType,
    "messageBody": context.messageBody
  })

@when('I encrypt <messageContent> as JSON string using AES with "{AESKey}" as passphrase and store it in <encryptedMessage>')
def step_impl(context,AESKey):
  context.AESKey = AESKey.strip().encode()
  context.encryptedMessage = AES(context.AESKey).encrypt(context.messageContent)

@when('I sign <encryptedMessage> using RSA-SHA256 with <identity> and signed timestamp from teleferic and store it on <messageSignature>')
def step_impl(context):
  
  context.executed = context.client.execute('''
    query{
      teleferic{
        signedTimestamp
      }
    }
  ''')
  assert not 'errors' in context.executed

  signable_object = OrderedDict()
  signable_object['messageHash'] = base64.b64encode(SHA256.new(context.encryptedMessage).digest())
  signable_object['timestamp'] = context.executed['data']['teleferic']['signedTimestamp']

  signable_object_format = msgpack.packb(signable_object)

  if context.messageSign != b'valid':
    signature = context.identity.sign(signable_object_format+b' ')
  else:
    signature = context.identity.sign(signable_object_format)

  context.signature = base64.b64encode(msgpack.packb({
    "signature": signature,
    "timestamp": context.executed['data']['teleferic']['signedTimestamp']
  }))


@when('I send <encryptedMessage> and <messageSignature> as public message to Teleferic')
def step_impl(context):
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
  
  if context.messageHash != b'valid':
    messageHash = SHA256.new(context.encryptedMessage+b' ')
  else:
    print('aca')
    messageHash = SHA256.new(context.encryptedMessage)

  if context.bodyHash != b'valid':
    bodyHash = SHA256.new(context.messageBody+b' ')
  else:
    bodyHash = SHA256.new(context.messageBody)

  if context.dossierHash != b'valid':
    dossierHash = HMAC.new(context.dossierSalt,context.messageBody+b' ',SHA256)
  else:  
    dossierHash = HMAC.new(context.dossierSalt,context.messageBody,SHA256)
  
  context.variables = {
    "sender": context.identity.address,
    "messageType": context.messageType.decode(),
    "messageHash": base64.b64encode(messageHash.digest()).decode(), 
    "dossierHash": base64.b64encode(dossierHash.digest()).decode(),
    "bodyHash": base64.b64encode(bodyHash.digest()).decode(),
    "messageSig": context.signature.decode(),
    "message": context.encryptedMessage.decode(),
  }
  context.executed = context.client.execute(context.query,variable_values=context.variables)

@then('the query response should be "{result}"')
def step_impl(context,result):
  print(json.dumps(context.variables))
  if result == 'success':
    assert context.executed.get('errors') == None
    assert {
      "data": {
        "sendMessage": {
          "messageHash": base64.b64encode(SHA256.new(context.encryptedMessage).digest()).decode()
        }
      }
    } == context.executed
  else:
    assert context.executed.get('errors') != None
