# -- FILE: features/steps/InviteNew.py
import base64
import msgpack
from collections import OrderedDict

from behave import given, when, then, step

from Crypto.Hash import SHA256, HMAC
from TelefericClient.Cryptography import AES, RSA
from TelefericClient import Client


@given('secret passphrase {passphrase}')
def step(context, passphrase):
    context.passphrase = passphrase.strip().encode()


@given('secret invite name {secretInviteName}')
def step_impl(context, secretInviteName):
    context.secretInviteName = secretInviteName.strip().encode()


@when('I encrypt using AES module and given passphrase')
def step_impl(context):
    cipher = AES(context.passphrase)
    context.InviteName = cipher.encrypt(context.secretInviteName)


@then('the resulting encrypted inviteName should be {inviteName}')
def step_impl(context, inviteName):
    assert context.InviteName == inviteName.strip().encode()


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


@then('resulting messageBody should be equal to {messageBody}')
def step_impl(context, messageBody):
    assert messageBody.strip().encode() == context.b64PackMessageBody


@given('message body content {messageBody}')
def step_impl(context, messageBody):
    context.b64PackMessageBody = messageBody.strip().encode()


@when('I decode message body with Base64')
def step_impl(context):
    context.packMessageBody = base64.b64decode(context.b64PackMessageBody)


@when('parse resulting message body with Message Pack')
def step_impl(context):
    context.messageBody = msgpack.unpackb(context.packMessageBody)


@then('{attribute} attribute should be {inviteName}')
def step_impl(context, attribute, inviteName):
    assert context.messageBody[attribute.strip().encode()] == inviteName.strip().encode()


@given('40 bytes random salt {dossierSalt}')
def step_imp(context, dossierSalt):
    parts = dossierSalt.replace(':', '')
    context.dossierSalt = bytes(bytearray.fromhex(parts))
    assert len(context.dossierSalt) == 40


@given('we encode dossierSalt with base64 as encodedDossierSalt')
def step_imp(context):
    context.encodedDossierSalt = base64.b64encode(context.dossierSalt)


@given('message body type <bodyType> equal to {code} ({name})')
def step_imp(context,code,name):
    context.bodyType = int(code)


@when('I compose invite message content sorting attributes alphabetically')
def step_imp(context):
    messageContent = OrderedDict()
    messageContent['bodyType'] = context.bodyType
    messageContent['dossierSalt'] = context.encodedDossierSalt
    messageContent['messageBody'] = context.b64PackMessageBody
    context.messageContent = messageContent


@when('format message content with Message Pack')
def step_imp(context):
    context.packMessageContent = msgpack.packb(context.messageContent)


@when('encrypt resulting message content pack using AES module with public passphrase "Peer Mountain"')
def step_imp(context):
    cipher = AES('Peer Mountain'.encode())
    context.b64EncryptedPackMessageContent = cipher.encrypt(context.packMessageContent) 


@then('resulting message should be {message}')
def step_imp(context, message):
    assert message.strip().encode() == context.b64EncryptedPackMessageContent

@given('message {message}')
def step_impl(context, message):
    context.message = message.strip().encode()


@when('I compute SHA256 hash of message content')
def step_impl(context):
    context.rawMessageHash = SHA256.new(context.message).digest()


@when('encode resulting message hash with Base64')
def step_impl(context):
    context.messageHash = base64.b64encode(context.rawMessageHash)


@then('resulting message content hash messageHash should be {messageHash}')
def step_imp(context, messageHash):
    assert context.messageHash == messageHash.strip().encode()


@when('I compute SHA256 hash of message body')
def step_imp(context):
    context.hashMessageBody = SHA256.new(context.b64PackMessageBody).digest()


@when('encode resulting message body hash with Base64')
def step_imp(context):
    context.b64HashMessageBody = base64.b64encode(context.hashMessageBody)


@then('resulting message body hash bodyHash should be {bodyHash}')
def step_imp(context, bodyHash):
    assert context.b64HashMessageBody == bodyHash.strip().encode()


@when('I compute HMAC-SHA256 hash of message body with given 40 bytes decoded salt')
def step_imp(context):
    decodedSalt = base64.b64decode(context.encodedDossierSalt)
    context.dossierHash = HMAC.new(decodedSalt, context.b64PackMessageBody, SHA256).digest()


@when('encode resulting message body hmac-hash with Base64')
def step_imp(context):
    context.b64DossierHash = base64.b64encode(context.dossierHash)


@then('resulting dossierHash should be {dossierHash}')
def step_imp(context, dossierHash):
    assert context.b64DossierHash == dossierHash.strip().encode()


@given('following private key <privkey>')
def step_impl(context):
    context.raw_privkey = context.text.strip()
    context.privkey = RSA(context.text.strip())


@given('messageHash {messageHash}')
def step_impl(context, messageHash):
    context.messageHash = messageHash.strip().encode()


@given('teleferic signed timestamp telefericSignedTimestamp')
def step_impl(context):
    client = Client()
    telefericSignedTimestamp = client.get_node_signedtimestamp()
    context.telefericSignedTimestamp = telefericSignedTimestamp.strip().encode()


@given('compose signable object')
def step_impl(context):
    context.signable_object = OrderedDict()
    context.signable_object['messageHash'] = context.messageHash
    context.signable_object['timestamp'] = context.telefericSignedTimestamp


@when('I format signable object with Message Pack')
def step_impl(context):
    context.formated_signable_object = msgpack.packb(context.signable_object)


@when('generate RSA signature <signature> using <privkey> of formated signable object')
def step_impl(context):
    context.signature = context.privkey.sign(context.formated_signable_object)


@when('compose signature object')
def step_impl(context):
    context.signature_object = OrderedDict()
    context.signature_object['signature'] = context.signature
    context.signature_object['timestamp'] = context.telefericSignedTimestamp


@when('format signature object with Message Pack')
def step_impl(context):
    context.format_signature_object = msgpack.packb(context.signature_object)


@when('encode resulted signature with Base64 into messageSign')
def step_impl(context):
    context.messageSign = base64.b64encode(context.format_signature_object)


@given('sender address {sender}')
def step_impl(context, sender):
    context.sender = sender.strip().encode()


@given('messageType {messageType}')
def step_impl(context, messageType):
    context.messageType = messageType.strip().encode()


@given('body hash {bodyHash}')
def step_impl(context, bodyHash):
    context.bodyHash = bodyHash.strip().encode()


@given('dossier hash {dossierHash}')
def step_impl(context, dossierHash):
    context.dossierHash = dossierHash.strip().encode()


@given('following mutation')
def step_impl(context):
    context.mutation = context.text.strip()


@when('I compose variable object')
def step_impl(context):
    import json
    vars = json.loads(context.text.strip())
    vars['messageSign'] = context.messageSign.decode()
    context.variables = json.dumps(vars)


@then('response should be success')
def step_impl(context):
    assert not 'errors' in context.query_response


@then('response should have messageHash property equal to {messageHash}')
def step_impl(context, messageHash):
    assert context.messageHash == messageHash.strip().encode()
