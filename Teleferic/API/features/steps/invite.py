# -- FILE: features/steps/invite.py
import os
from behave import given, when, then, step

from Crypto.PublicKey import RSA as Key
from Crypto.Hash import HMAC, SHA256
from libs.tools import RSA, AES, Identity

import json

@given('registred Identity stored in <identity>')
def step_impl(context):
  context.identity = Identity(context.REGISTRED_IDENTITY)

@given('Teleferic has pubkey <telefericPubkey>')
def step_impl(context):
  context.execute_steps('''
      When I query the pubkey of Teleferic
  ''')
  context.telefericPubkey = Key.importKey(context.executed['data']['teleferic']['persona']['pubkey'])

@given('bootstrap url is "{bootstrapNode}"')
def step_impl(context,bootstrapNode):
  if bootstrapNode == 'None':
    context.bootstrapNode = None
  else:
    context.bootstrapNode = bootstrapNode

@given('bootstrap PM-Address is "{bootstrapAddr}"')
def step_impl(context,bootstrapAddr):
  if bootstrapAddr == 'None':
    context.bootstrapAddr = None
  else:
    context.bootstrapAddr = bootstrapAddr

@given('offering PM-Address is "{offeringAddr}"')
def step_impl(context, offeringAddr):
  if offeringAddr == 'None':
    context.offeringAddr = None
  else:
    context.offeringAddr = offeringAddr

@given('service offering ID is "{serviceOfferingID}"')
def step_impl(context, serviceOfferingID):
  if serviceOfferingID == 'None':
    context.serviceOfferingID = None
  else:
    context.serviceOfferingID = serviceOfferingID

@given('service announcement message is "{serviceAnnouncementMessage}"')
def step_impl(context,serviceAnnouncementMessage):
  if serviceAnnouncementMessage == 'None':
    context.serviceAnnouncementMessage = None
  else:
    context.serviceAnnouncementMessage = serviceAnnouncementMessage

@given('invitation name is "{inviteName}"')
def step_impl(context,inviteName):
  if inviteName == 'None':
    context.inviteName = None
  else:
    context.inviteName = inviteName

@given('invitation key is "{inviteKey}"')
def step_impl(context,inviteKey):
  if inviteKey == 'None':
    context.inviteKey = None
  else:
    context.inviteKey = inviteKey

@given('dossier salt is "{dossierSalt}"')
def step_impl(context, dossierSalt):
  context.dossierSalt = dossierSalt

@given('dossier hash is "{dossierHash}"')
def step_impl(context,dossierHash):
  context.dossierHash = dossierHash

@given('message hash is "{messageHash}"')
def step_impl(context,messageHash):
  context.messageHash = messageHash

@given('message sign is "{messageSign}"')
def step_impl(context,messageSign):
  context.messageSign = messageSign

@given('body hash is "{bodyHash}"')
def step_impl(context,bodyHash):
  context.bodyHash = bodyHash

@given('message type is "{messageType}", and is stored in <messageType>')
def step_impl(context, messageType):
  context.messageType = messageType

@given('message body type is "{bodyType}", and is stored in <bodyType>')
def step_impl(context, bodyType):
  context.bodyType = bodyType

@when('I encrypt "{inviteName}" using AES-256 with {inviteKey} and store it on <encryptedInviteName>')
def step_impl(context, inviteName, inviteKey):
  cipher = AES(context.inviteKey)
  context.encryptedInviteName = cipher.encrypt(context.inviteName).decode()

@when('I compose invitation message with <encryptedInviteName>, {bootstrapNode}, {offeringAddr}, {serviceAnnouncementMessage}, {serviceOfferingID} and {inviteName}. And I store it in <messageBody>')
def step_impl(context, **args):
  context.messageBody = json.dumps({
    "bootstrapNode": context.bootstrapNode,
    "bootstrapAddr": context.bootstrapAddr,
    "offeringAddr": context.offeringAddr,
    "serviceAnnouncementMessage": context.serviceAnnouncementMessage,
    "serviceOfferingID": context.serviceOfferingID,
    "inviteName": context.encryptedInviteName
  })

@when('I compose message content with {dossierSalt}, <bodyType> and <messageBody>. And I store it in <messageContent>')
def step_impl(context, **args):
  context.messageContent = json.dumps({
    "dossierSalt": context.dossierSalt,
    "bodyType": int(context.bodyType),
    "messageBody": context.messageBody
  })

@when('I encrypt <messageContent> as JSON string using AES with "{AESKey}" as passphrase and store it in <encryptedMessage>')
def step_impl(context,AESKey):
  context.AESKey = AESKey
  context.encryptedMessage = AES(AESKey).encrypt(context.messageContent).decode()

@when('I sign <encryptedMessage> using RSA-SHA256 with <identity> and store it on <messageSignature>')
def step_impl(context):
  if context.messageSign != 'valid':
    context.messageSign = context.identity.sign(context.encryptedMessage.encode()+b' ').decode()
  else:
    context.messageSign = context.identity.sign(context.encryptedMessage.encode()).decode()

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
  
  if context.messageHash != 'valid':
    messageHash = SHA256.new(context.encryptedMessage.encode()+b' ')
  else:
    messageHash = SHA256.new(context.encryptedMessage.encode())

  if context.bodyHash != 'valid':
    bodyHash = SHA256.new(context.messageBody.encode()+b' ')
  else:
    bodyHash = SHA256.new(context.messageBody.encode())

  if context.dossierHash != 'valid':
    dossierHash = HMAC.new(context.dossierSalt.encode(),context.messageBody.encode()+b' ',SHA256)
  else:  
    dossierHash = HMAC.new(context.dossierSalt.encode(),context.messageBody.encode(),SHA256)
  
  context.variables = {
    "sender": context.identity.address,
    "messageType": context.messageType,
    "messageHash": messageHash.hexdigest(), 
    "dossierHash": dossierHash.hexdigest(),
    "bodyHash": bodyHash.hexdigest(),
    "messageSig": context.messageSign,
    "message": context.encryptedMessage,
  }
  context.executed = context.client.execute(context.query,variable_values=context.variables)

@then('the query response should be "{result}"')
def step_impl(context,result):
  if result == 'success':
    assert context.executed.get('errors') == None
    assert {
      "data": {
        "sendMessage": {
          "messageHash": SHA256.new(context.encryptedMessage.encode()).hexdigest()
        }
      }
    } == context.executed
  else:
    assert context.executed.get('errors') != None
