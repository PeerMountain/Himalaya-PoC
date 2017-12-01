# -- FILE: features/steps/Identity.py
import os
from behave import given, when, then, step

from TelefericClient import Identity
from TelefericClient.Cryptography import RSA
import base64

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
  identity = Identity(context.key.key)
  assert identity.address == address.strip()

@when(u'I encode the key it with Base64')
def step_impl(context):
    raw_key = context.key.key.exportKey('PEM')
    context.encoded_key = base64.b64encode(raw_key)

@then(u'resulting string should be {result}')
def step_impl(context,result):
    print(context.encoded_key)
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