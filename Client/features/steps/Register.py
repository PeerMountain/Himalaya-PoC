# -- FILE: features/steps/Register.py
import os
from behave import given, when, then, step

from TelefericClient.Cryptography import AES, RSA
from Crypto.Hash import SHA256, HMAC

from collections import OrderedDict
import msgpack
import base64


@given('invite key {inviteKey}')
def step_impl(context, inviteKey):
    context.inviteKey = inviteKey.strip().encode()


@given(u'Teleferic pubkey from {bootstrapNode}')
def step_impl(context, bootstrapNode):
    context.execute_steps("""
        Given following query
        '''
        query{
            teleferic{
                persona{
                    pubkey
                }
            }
        }
        '''
        And bootstrap node url %s
        When I send query to bootstrap node
        And get property data.teleferic.persona.pubkey from query response
        And decode property with Base64
    """ % bootstrapNode.strip())
    context.teleferic_pubkey = context.property


@when(u'I encrypt inviteKey using RSA module and given pubkey')
def step_impl(context):
    cipher = RSA(context.teleferic_pubkey)
    context.keyProof = cipher.encrypt(context.inviteKey)


@then(u'the resulting encrypted <keyProof> should be {result}')
def step_impl(context, result):
    assert context.keyProof == result.strip().encode()


@given('invite name {baseInviteName}')
def step_impl(context, baseInviteName):
    context.baseInviteName = baseInviteName.strip().encode()


@when(u'I encrypt baseInviteName using RSA module and given pubkey')
def step_impl(context):
    cipher = RSA(context.teleferic_pubkey)
    context.encryptedInviteName = cipher.encrypt(context.baseInviteName)


@given(u'valid invite persisted with identifier message hash {inviteMsgID}')
def step_impl(context, inviteMsgID):
    context.inviteMsgID = inviteMsgID.strip().encode()


@given(u'RSA encrypted with pubkey of {bootstrapNode} bootstrap node of {inviteKey} as <keyProof>')
def step_impl(context, bootstrapNode, inviteKey):
    context.execute_steps('''
        Given Teleferic pubkey from %s
    ''' % bootstrapNode.strip())
    encoded_inviteKey = inviteKey.strip().encode()
    cipher = RSA(context.teleferic_pubkey)
    context.keyProof = cipher.encrypt(encoded_inviteKey)


@given(u'RSA encrypted with pubkey of {bootstrapNode} bootstrap node of {inviteName} as <nameProof>')
def step_impl(context, bootstrapNode, inviteName):
    context.execute_steps('''
        Given Teleferic pubkey from %s
    ''' % bootstrapNode.strip())
    encoded_inviteName = inviteName.strip().encode()
    cipher = RSA(context.teleferic_pubkey)
    context.nameProof = cipher.encrypt(encoded_inviteName)


@given(u'Base64 decoded version of {pubKey} as <publicKey>')
def step_impl(context, pubKey):
    context.publicKey = base64.b64decode(pubKey.strip().encode())
    key = RSA(context.publicKey)
    assert key.key.has_private() == False


@given(u'nickename string {nickname} as <publicNickname>')
def step_impl(context, nickname):
    context.publicNickname = nickname.strip().encode()


@when(u'I pack following registration message body shape')
def step_impl(context):
    aux = OrderedDict()
    aux["inviteMsgID"] = context.inviteMsgID
    aux["keyProof"] = context.keyProof
    aux["inviteName"] = context.nameProof
    aux["publicKey"] = context.publicKey
    aux["publicNickname"] = context.publicNickname
    context.pack = msgpack.packb(aux)


@when(u'encode the pack with Base64')
def step_impl(context):
    context.encoded_pack = base64.b64encode(context.pack)


@then(u'<messageBody> should be {result}')
def step_impl(context, result):
    assert context.encoded_pack == result.strip().encode()


@when(u'I compose resgiter message content with following shape')
def step_impl(context):
    messageContent = OrderedDict()
    messageContent['bodyType'] = context.bodyType
    messageContent['dossierSalt'] = context.dossierSalt
    messageContent['messageBody'] = context.b64PackMessageBody
    context.messageContent = messageContent


@given(u'following private key encoded in Base64 {privkey}')
def step_impl(context, privkey):
    context.privkey = RSA(base64.b64decode(privkey.strip().encode()))


@given(u'signed timestamp from bootstrap node {bootstrapNode}')
def step_impl(context, bootstrapNode):
    context.execute_steps("""
    Given bootstrap node url %s
    And bootstrap node pubkey <bootstrapNodePubkey>
    And following query
    '''
    query{
        teleferic{
            signedTimestamp
        }
    }
    ''' 
    When I send query to bootstrap node
    And get property data.teleferic.signedTimestamp from query response
    """ % bootstrapNode.strip())
    context.telefericSignedTimestamp = context.property_value


@when(u'generate RSA signature <signature> using {privkey} of formated signable object')
def step_impl(context, privkey):
    context.signature = context.privkey.sign(context.formated_signable_object)
