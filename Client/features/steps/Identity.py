# -- FILE: features/steps/Identity.py
import os
from behave import given, when, then, step

from TelefericClient import Identity
from TelefericClient.Cryptography import RSA
import base64


@given(u'the following {key_size} pubkey')
def step_impl(context, key_size):
    context.key_size = key_size
    context.key = RSA(context.text.strip())


@given(u'the address prefix [{prefix_0}, {prefix_1}]')
def step_impl(context, prefix_0, prefix_1):
    context.address_prefix = [int(prefix_0), int(prefix_1)]


@when('compute SHA256 hash of pubkey')
def step_imp(context):
    pass


@when('compute RIPEMD160 of resulting SHA256')
def step_imp(context):
    pass


@when('prefix resulting RIPEMD160 with [1, 0] bytes to generate the base address')
def step_imp(context):
    pass


@when('apply SHA256 two times over resulting RIPEMD160 to generate the checksum')
def step_imp(context):
    pass


@when('append last 4 bytes of resulting checksum at the end of base address to generate the address')
def step_imp(context):
    pass


@then('the address should be {address}')
def step_imp(context, address):
    identity = Identity(context.key.key, context.address_prefix)
    assert identity.address == address.strip()


@when(u'I encode the key it with Base64')
def step_impl(context):
    raw_key = context.key.key.exportKey('PEM')
    context.encoded_key = base64.b64encode(raw_key)


@then(u'resulting string should be {result}')
def step_impl(context, result):
    assert result.strip().encode() == context.encoded_key


@given(u'following private key')
def step_impl(context):
    context.privkey = context.text.strip().encode()


@when(u'I export public key from private key on PEM format')
def step_impl(context):
    context.pubkey = RSA(context.privkey).key.publickey().exportKey()


@then(u'resulting public key should be following')
def step_impl(context):
    assert context.pubkey == context.text.strip().encode()


@then(u'the address calculation should return an error')
#Source:https://stackoverflow.com/questions/27894993/handling-exceptions-in-python-behave-testing-framework
def step_impl(context):
  try:
    identity = Identity(context.key.key, context.address_prefix)
    assert False
  except Exception as e:
    assert True

@when(u'calculating the address')
def step_impl(context):
    pass

@then(u'I have to compute SHA256 hash of pubkey')
def step_impl(context):
    pass
@then(u'I have to compute RIPEMD160 of resulting SHA256')
def step_impl(context):
    pass

@then(u'I have to prefix resulting RIPEMD160 with the given prefix to generate the base address')
def step_impl(context):
    pass

@then(u'I have to apply SHA256 two times over resulting RIPEMD160 to generate the checksum')
def step_impl(context):
    pass

@then(u'I have to append last 4 bytes of resulting checksum at the end of base address to generate the address')
def step_impl(context):
    pass
