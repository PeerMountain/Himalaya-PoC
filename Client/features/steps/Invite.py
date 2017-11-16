# -- FILE: features/steps/Invite.py
import os
from behave import given, when, then, step

from TelefericClient.Cryptography import AES

from collections import OrderedDict
import msgpack
import base64

@given('secret passphrase {passphrase}')
def step_impl(context,passphrase):
  context.passphrase = passphrase.strip().encode()
  print(len(context.passphrase))
  assert len(context.passphrase) == 32

@given('secret invite name {inviteName}')
def step_impl(context, inviteName):
  context.inviteName = inviteName.strip().encode()

@when('I encrypt using AES module and given passphrase')
def step_impl(context):
  cipher = AES(context.passphrase)
  context.encryptedInviteName = cipher.encrypt(context.inviteName)

@then('the resulting encrypted invite name should be {result}')
def step_impl(context, result):
  print(context.encryptedInviteName)
  assert context.encryptedInviteName == result.strip().encode()  

@given('a bootstrap node url {bootstrapNode}')
def step_impl(context,bootstrapNode):
  context.bootstrapNode = bootstrapNode.strip().encode()

@given('bootstrap addrress {bootstrapAddr}')
def step_impl(context,bootstrapAddr):
  context.bootstrapAddr = bootstrapAddr.strip().encode()

@given('offering registred Persona address {offeringAddr} (Rigth now only teleferic Persona is registred)')
def step_impl(context,offeringAddr):
  context.offeringAddr = offeringAddr.strip().encode()

@given('service announcement message SHA256 hash identifier encoded on Base64 {serviceAnnouncementMessage} (not defined yet)')
def step_impl(context,serviceAnnouncementMessage):
  context.serviceAnnouncementMessage = serviceAnnouncementMessage.strip().encode()

@given('service identifier {serviceOfferingID}')
def step_impl(context,serviceOfferingID):
  context.serviceOfferingID = serviceOfferingID.strip().encode()

@given('encrypted invite name {inviteName}')
def step_impl(context,inviteName):
  context.encryptedInviteName = inviteName.strip().encode()

@when('I compose invite message body sorting attributes alphabetically')
def step_impl(context):
  messageBody = OrderedDict()
  messageBody['bootstrapAddr'] = context.bootstrapAddr
  messageBody['bootstrapNode'] = context.bootstrapNode
  messageBody['inviteName'] = context.encryptedInviteName
  messageBody['offeringAddr'] = context.offeringAddr
  messageBody['serviceAnnouncementMessage'] = context.serviceAnnouncementMessage
  messageBody['serviceOfferingID'] = context.serviceOfferingID
  context.messageBody = messageBody

@when('format message body with Message Pack')
def step_impl(context):
  context.packMessageBody = msgpack.packb(context.messageBody)

@when('encode resulting pack with Base64')
def step_impl(context):
  context.b64PackMessageBody = base64.b64encode(context.packMessageBody)

@then('resulting message body should be equal to {result}')
def step_impl(context,result):
  assert result.strip().encode() == context.b64PackMessageBody

@given('message body {result}')
def step_impl(context, result):
  context.b64PackMessageBody = result.strip().encode()

@when('I decode message boy with Base64')
def step_impl(context):
  context.packMessageBody = base64.b64decode(context.b64PackMessageBody)

@when('parse resulting content with Message Pack')
def step_impl(context):
  context.messageBody = msgpack.unpackb(context.packMessageBody)

@then('{attribute} attribute should be {value}')
def step_impl(context,attribute,value):
  assert context.messageBody[attribute.strip().encode()] == value.strip().encode()