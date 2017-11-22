# -- FILE: features/steps/Invite.py
import os
from behave import given, when, then, step

from TelefericClient.Cryptography import AES, RSA
from Crypto.Hash import SHA256, HMAC

from collections import OrderedDict
import msgpack
import base64


@given('secret passphrase {passphrase}')
def step_impl(context, passphrase):
    context.passphrase = passphrase.strip().encode()
    assert len(context.passphrase) == 32


@given('secret invite name {inviteName}')
def step_impl(context, inviteName):
    context.inviteName = inviteName.strip().encode()


@when('I encrypt using AES module and given passphrase')
def step_impl(context):
    cipher = AES(context.passphrase)
    context.encryptedInviteName = cipher.encrypt(context.inviteName)


@then('the resulting encrypted <inviteName> should be {result}')
def step_impl(context, result):
    assert context.encryptedInviteName == result.strip().encode()


@given('a bootstrap node url {bootstrapNode}')
def step_impl(context, bootstrapNode):
    context.bootstrapNode = bootstrapNode.strip().encode()


@given('bootstrap addrress {bootstrapAddr}')
def step_impl(context, bootstrapAddr):
    context.bootstrapAddr = bootstrapAddr.strip().encode()


@given('offering registred Persona address {offeringAddr} (Rigth now only teleferic Persona is registred)')
def step_impl(context, offeringAddr):
    context.offeringAddr = offeringAddr.strip().encode()


@given('service announcement message SHA256 hash identifier encoded on Base64 {serviceAnnouncementMessage} (not defined yet)')
def step_impl(context, serviceAnnouncementMessage):
    context.serviceAnnouncementMessage = serviceAnnouncementMessage.strip().encode()


@given('service identifier {serviceOfferingID}')
def step_impl(context, serviceOfferingID):
    context.serviceOfferingID = serviceOfferingID.strip().encode()


@given('encrypted invite name {inviteName}')
def step_impl(context, inviteName):
    context.encryptedInviteName = inviteName.strip().encode()


@when('I compose invite message body sorting attributes alphabetically')
def step_impl(context):
    messageBody = OrderedDict()
    messageBody['bootstrapAddr'] = context.bootstrapAddr
    messageBody['bootstrapNode'] = context.bootstrapNode
    messageBody['inviteName'] = context.encryptedInviteName
    messageBody['offeringAddr'] = context.offeringAddr
    messageBody[
        'serviceAnnouncementMessage'] = context.serviceAnnouncementMessage
    messageBody['serviceOfferingID'] = context.serviceOfferingID
    context.messageBody = messageBody


@when('format message body with Message Pack')
def step_impl(context):
    context.packMessageBody = msgpack.packb(context.messageBody)


@when('encode resulting message body pack with Base64')
def step_impl(context):
    context.b64PackMessageBody = base64.b64encode(context.packMessageBody)


@then('resulting <messageBody> should be equal to {result}')
def step_impl(context, result):
    assert result.strip().encode() == context.b64PackMessageBody


@given('message body content {result}')
def step_impl(context, result):
    context.b64PackMessageBody = result.strip().encode()


@when('I decode message body with Base64')
def step_impl(context):
    context.packMessageBody = base64.b64decode(context.b64PackMessageBody)


@when('parse resulting message body with Message Pack')
def step_impl(context):
    context.messageBody = msgpack.unpackb(context.packMessageBody)


@then('{attribute} attribute should be {value}')
def step_impl(context, attribute, value):
    assert context.messageBody[
        attribute.strip().encode()] == value.strip().encode()


@given('40 bytes random salt {dossierSalt}')
def step_imp(context, dossierSalt):
    parts = dossierSalt.replace(':', '')
    context.dossierSalt = bytes(bytearray.fromhex(parts))
    assert len(context.dossierSalt) == 40


@given('message body type <bodyType> equal to 0 (Invitation)')
def step_imp(context):
    context.bodyType = 0


@when('I compose invite message content sorting attributes alphabetically')
def step_imp(context):
    messageContent = OrderedDict()
    messageContent['bodyType'] = context.bodyType
    messageContent['dossierSalt'] = context.dossierSalt
    messageContent['messageBody'] = context.b64PackMessageBody
    context.messageContent = messageContent


@when('format message content with Message Pack')
def step_imp(context):
    context.packMessageContent = msgpack.packb(context.messageContent)


@when('encrypt resulting message content pack using AES with public passphrase "Peer Mountain"')
def step_imp(context):
    cipher = AES('Peer Mountain'.encode())
    context.encryptedPackMessageContent = cipher.encrypt(
        context.packMessageContent)


@when('encode resulting encrypted message content pack with Base64')
def step_imp(context):
    context.b64EncryptedPackMessageContent = base64.b64encode(
        context.encryptedPackMessageContent)


@then('resulting <message> should be {result}')
def step_imp(context, result):
    assert result.strip().encode() == context.b64EncryptedPackMessageContent

@when(u'I compute SHA256 hash of message content')
def step_impl(context):
  context.rawMessageHash = SHA256.new(context.message).digest()


@when(u'encode resulting message hash with Base64')
def step_impl(context):
    context.messageHash = base64.b64encode(context.rawMessageHash)

@then('resulting message content hash <messageHash> should be {result}')
def step_imp(context, result):
    assert context.messageHash == result.strip().encode()

@when('I compute SHA256 hash of message body')
def step_imp(context):
    context.hashMessageBody = SHA256.new(context.b64PackMessageBody).digest()


@when('encode resulting message body hash with Base64')
def step_imp(context):
    context.b64HashMessageBody = base64.b64encode(context.hashMessageBody)


@then('resulting message body hash <bodyHash> should be {result}')
def step_imp(context, result):
    assert context.b64HashMessageBody == result.strip().encode()


@when('I compute HMAC-SHA256 hash of message body with given 40bytes salt')
def step_imp(context):
    context.dossierHash = HMAC.new(
        context.dossierSalt, context.b64PackMessageBody, SHA256).digest()


@when('encode resulting message body hmac-hash with Base64')
def step_imp(context):
    context.b64DossierHash = base64.b64encode(context.dossierHash)


@then('resulting <dossierHash> should be {result}')
def step_imp(context, result):
    assert context.b64DossierHash == result.strip().encode()


@given(u'following private key <privkey>')
def step_impl(context):
    context.privkey = RSA(context.text.strip())


@given(u'message hash {messageHash}')
def step_impl(context, messageHash):
    context.messageHash = messageHash.strip().encode()


@given(u'teleferic signed timestamp {telefericSignedTimestamp}')
def step_impl(context, telefericSignedTimestamp):
    context.telefericSignedTimestamp = telefericSignedTimestamp.strip().encode()


@given(u'compose signable object')
def step_impl(context):
    context.signable_object = OrderedDict()
    context.signable_object['messageHash'] = context.messageHash
    context.signable_object['timestamp'] = context.telefericSignedTimestamp


@when(u'I format signable object with Message Pack')
def step_impl(context):
    context.formated_signable_object = msgpack.packb(context.signable_object)
    print('asas',context.formated_signable_object)


@when(u'generate RSA signature <signature> using <privkey> of formated signable object')
def step_impl(context):
    context.signature = context.privkey.sign(context.formated_signable_object)


@when(u'compose signature object')
def step_impl(context):
    context.signature_object = OrderedDict()
    context.signature_object['signature'] = context.signature
    context.signature_object['timestamp'] = context.telefericSignedTimestamp


@when(u'format signable object with Message Pack')
def step_impl(context):
    context.format_signature_object = msgpack.packb(
        context.signature_object)


@when(u'encode resulted signature with Base64')
def step_impl(context):
    context.b64encoded_format_signature_object = base64.b64encode(
        context.format_signature_object)


@then(u'resulting <messageSig> should be {result}')
def step_impl(context, result):
    print(context.b64encoded_format_signature_object)
    assert context.b64encoded_format_signature_object == result.strip().encode()


@given(u'dossier hash {dossierHash}')
def step_impl(context, dossierHash):
    context.dossierHash = dossierHash.strip().encode()


@given(u'following mutation')
def step_impl(context):
    context.mutation = context.text.strip()


@given(u'sender address {sender}')
def step_impl(context, sender):
    context.sender = sender.strip().encode()


@given(u'message type {messageType}')
def step_impl(context, messageType):
    context.messageType = messageType.strip().encode()


@given(u'body hash {bodyHash}')
def step_impl(context, bodyHash):
    context.bodyHash = bodyHash.strip().encode()


@given(u'message signature {messageSig}')
def step_impl(context, messageSig):
    context.messageSig = messageSig.strip().encode()


@given(u'message {message}')
def step_impl(context, message):
    context.message = message.strip().encode()


@when(u'I compose variable object')
def step_impl(context):
    context.variables = context.text.strip()


@then(u'response should be success')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then response should be success')


@then(u'response should have cacheTXID property')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then response should have cacheTXID property')
