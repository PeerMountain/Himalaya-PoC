import base64
import os
import time
from collections import OrderedDict

import msgpack
from behave import given, when, then
from Crypto.Hash import SHA256

from API.Mock import Reader, Teleferic_Identity
from API.Mock.Authorizer.constants import Parameters
from libs.tools import Identity


@given('we unpack and decode the {envelope} as envelope')
def step(context, envelope):
    context.envelope = msgpack.unpackb(base64.b64decode(envelope.encode()))


@then('we check if the message already exists')
def step(context):
    file_path = context.envelope.get(b'messageHash')
    assert not os.path.isfile(file_path)


@then('we check if the sender is registered')
def step(context):
    sender = Reader.get_persona(context.envelope.get(b'sender'))
    assert sender
    context.sender = sender


@then('we check if the messageHash is valid')
def step(context):
    message = context.envelope.get(b'message')
    message_hash = context.envelope.get(b'messageHash')

    assert SHA256.new(message).digest() == message_hash


@then('we check if the message timestamp was signed by Teleferic')
def step(context):
    teleferic_signature = msgpack.unpackb(base64.b64decode(
        context.envelope.get(b'messageSig')[b'timestamp']
    ))

    assert Teleferic_Identity.verify_signature(
        teleferic_signature[b'timestamp'],
        teleferic_signature[b'signature'],
    )


@then('we check if message signature is indeed from the sender')
def step(context):
    identity = Identity(context.sender.pubkey)

    validator = OrderedDict()
    validator['messageHash'] = base64.b64encode(context.envelope.get(b'messageHash'))
    validator['timestamp'] = context.envelope.get(b'messageSig')[b'timestamp']
    packed_validator = msgpack.packb(validator)

    assert identity.verify(
        packed_validator,
        context.envelope.get(b'messageSig')[b'signature']
    )


@then('we check if the ACLs are valid')
def step(context):
    # There's just one ACL in the message
    acl_reader = context.envelope.get(b'ACL')[0][b'reader']
    assert Reader.get_persona(address=acl_reader)



@given('we create a variable named containers for the containers')
def step(context):
    # There's just one container in the message
    context.container = context.envelope.get(b'containers')[0]


@then('we check if the containers hash are valid')
def step(context):
    container_hash = context.container.get(b'containerHash')
    object_container = context.container.get(b'objectContainer')
    assert container_hash == SHA256.new(object_container).digest()


@then('we check if the containers signature are valid')
def step(context):
    identity = Identity(context.sender.pubkey)
    container_hash = context.container.get(b'containerHash')
    container_signature = context.container.get(b'containerSig')

    validator = OrderedDict()
    validator['messageHash'] = base64.b64encode(container_hash)
    validator['timestamp'] = container_signature.get(b'timestamp')
    packed_validator = msgpack.packb(validator)

    assert identity.verify(packed_validator, container_signature.get(b'signature'))
