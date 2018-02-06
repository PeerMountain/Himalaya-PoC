import json
import random
import base64
import os
import time
from collections import OrderedDict

import msgpack
import requests
from behave import given, when, then
from Crypto.Hash import SHA256, HMAC

from API.Mock import Reader, Teleferic_Identity
from API.Mock.Authorizer.constants import Parameters
from libs.tools import Identity, AES


@given('sender Identity as sender')
def step(context):
    context.sender = Identity(context.REGISTRED_IDENTITY)


@given('reader Identity as reader')
def step(context):
    context.reader = Identity(context.public_4096_a)


@given('valid_until date as {valid_until}')
def step(context, valid_until):
    context.valid_until = valid_until
       

@given('retain_until date as {retain_until}')
def step(context, retain_until):
    context.retain_until = retain_until
       

@given('object as {object}')
def step(context, object):
    context.object = object.encode()
       

@given('metas using {meta_keys} and {meta_values}')
def step(context, meta_keys, meta_values):
    meta_keys = meta_keys.split(',')
    meta_values = meta_values.split(',')

    metas = [
        OrderedDict(**{
            'metaKey': key,
            'metaValue':value,
        }) for key, value in zip(meta_keys, meta_values)
    ]
    
    context.metas = metas


@given('container_hash as {container_hash}')
def step(context, container_hash):
    context.container_hash = container_hash


@given('container_key as {container_key}')
def step(context, container_key):
    context.container_key = container_key.encode()


@given('object_hash as {object_hash}')
def step(context, object_hash):
    context.object_hash = object_hash


@given('result as {result}')
def step(context, result):
    context.result = result


@when('we build the assertion list')
def step(context):
    context.raw_assertions = [
        {
            'valid_until': context.valid_until,
            'retain_until': context.retain_until,
            'object': context.object,
            'metas': [
                context.metas
            ]
        }
    ]

    cipher = AES(context.container_key)
    context.object_container = cipher.encrypt(context.object)

    context.object_hash = base64.b64encode(
        SHA256.new(context.object).digest()
    ).decode()

    context.container_hash = base64.b64encode(
        SHA256.new(context.object_container).digest()
    )
        
    object_signature = context.sender.sign_message(context.object_hash)
    container_signature = context.sender.sign_message(context.container_hash)

    context.assertions = [{
        'validUntil': context.valid_until,
        'retainUntil': context.retain_until,
        'containerHash': context.container_hash.decode(),
        'containerKey': context.container_key,
        'objectHash': context.object_hash,
        'objectSign': object_signature, 
        'metas': context.metas,
        'container': context.object_container,
        'containerSignature': container_signature,
    }]
    

@when('we build the salted meta hash list using {meta_salt}')
def step(context, meta_salt):
    meta_salt = meta_salt.encode()
    salted_meta_hashes = []

    for meta in context.metas:
        pack = msgpack.packb(meta_salt)
        salted_meta_hash = base64.b64encode(
            HMAC.new(
                meta_salt, pack, SHA256
            ).digest()
        )

        meta.update({
            'metaSalt': meta_salt,
        })

        salted_meta_hashes.append(salted_meta_hash.decode())

    context.salted_meta_hashes = list(salted_meta_hashes)


@when('we build the container list')
def step(context):
    context.containers = []

    for i, assertion in enumerate(context.assertions):
        context.containers.append({
            'containerHash': assertion.get('containerHash'),
            # 'objectHash': assertion.get('objectHash'),
            'containerSign': assertion.pop('containerSignature'),
            # 'saltedMetaHashes': context.salted_meta_hashes[i],
            'objectContainer': assertion.pop('container')
        })


@when('we build the message body')        
def step(context):
    context.message_body = {
        'subject': context.sender.address,
        'assertions': context.assertions,
    }
    context.packed_message_body = msgpack.packb(context.message_body)
    context.body_hash = base64.b64encode(SHA256.new(
        context.packed_message_body
    ).digest())

    context.dossier_salt = "".join([
        chr(random.randint(0, 255))
        for _ in range(int(40))
    ]).encode()

    context.dossier_hash = base64.b64encode(
        HMAC.new(context.dossier_salt, context.packed_message_body, SHA256).digest()
    )


@when('we build the message content with {message_key}')
def step(context, message_key):
    body_type = 0
    context.message_key = message_key
    message_body_signature = context.sender.sign_message(
        context.packed_message_body
    )
    message_content = {
        'bodyType': body_type,
        'dossierSalt': context.dossier_hash,
        'messageBody': context.packed_message_body,
        'signature':  message_body_signature,
    }

    context.packed_message_content = msgpack.packb(message_content)

    aes = AES(message_key.encode())
    context.encrypted_message_content = aes.encrypt(context.packed_message_content)
    context.message_hash =  base64.b64encode(SHA256.new(
        context.encrypted_message_content
    ).digest())


@when('we build the message')
def step(context):
    context.encrypted_message_key = context.reader.encrypt(context.message_key.encode())
    context.acl_rule_list = [{
        'reader': context.reader.address,
        'key': context.encrypted_message_key,
    }]

    context.container_sign = context.sender.sign_message(
        context.container_hash,
    )

    context.container_data_list = [{
        'objectHash': context.object_hash,
        'container': {
            'containerHash': context.container_hash.decode(),
            'containerSign': context.container_sign,
            'objectContainer': context.object_container.decode(),
        },
        'metaHashes': context.salted_meta_hashes,
    }]

    context.message_sign = context.sender.sign_message(
        context.message_hash,
    )

    context.message_envelope = {
        'sender': context.sender.address,
        'messageType': 'ASSERTION',
        'ACL': context.acl_rule_list,
        'objects': context.container_data_list,
        'messageHash': context.message_hash.decode(),
        'messageSign': context.message_sign,
        'dossierHash': context.dossier_hash.decode(),
        'bodyHash': context.body_hash.decode(),
        'message': context.encrypted_message_content.decode(),
    }


@when('we build the query')
def step(context):
    context.query = """
    mutation (
        $sender: Address!
        $messageType: MessageType!
        $messageHash: SHA256!
        $bodyHash: SHA256!
        $messageSign: Sign!
        $message: AESEncryptedBlob!
        $dossierHash: HMACSHA256!
        $ACL: [ACLRule]
        $objects: [ObjectInput]
        ){
        sendMessage(
            envelope: {
                sender: $sender
                messageType: $messageType
                messageHash: $messageHash
                bodyHash: $bodyHash
                messageSign: $messageSign
                message: $message
                dossierHash: $dossierHash
                objects: $objects
                ACL: $ACL
            }
        ) {
            messageHash
        }
    }
    """


@when('we send the assertion to Teleferic')
def step(context):
    context.response = context.client.execute(
        context.query,
        variable_values=context.message_envelope
    )


@then('the query response is equal to result')
def step(context):
    if context.result == 'success':
        assert not context.response.get('errors')

        response_message_hash = base64.b64encode(SHA256.new(
            context.encrypted_message_content
        ).digest()).decode()

        assert {
          'data': {
            'sendMessage': {
              'messageHash': response_message_hash,
            }
          }
        } == context.response

    else:
        assert context.response.get('errors')


@then('we check if the sender is registered')
def step(context):
    # There's just one ACL in the message, with one sender
    acl_sender = context.message_body['subject']
    assert Reader.get_persona(address=acl_sender)


@then('we check if the reader is registered')
def step(context):
    # There's just one ACL in the message, with one reader
    acl_reader = context.message_envelope.get('ACL')[0]['reader']
    assert Reader.get_persona(address=acl_reader)


@then('we check if the message timestamp was signed by Teleferic')
def step(context):
    message_sig = msgpack.unpackb(base64.b64decode(
        context.message_envelope.get('messageSign')
    ))
    teleferic_signature = msgpack.unpackb(base64.b64decode(
        message_sig.get(b'timestamp')
    ))

    assert Teleferic_Identity.verify_signature(
        teleferic_signature[b'timestamp'],
        teleferic_signature[b'signature'],
    )
