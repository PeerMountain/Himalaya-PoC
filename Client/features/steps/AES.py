# -- FILE: features/steps/AES.py
import os
from behave import given, when, then, step

from TelefericClient.Cryptography import AES

@given('a passphrase {key}')
def step_imp(context, key):
  context.passphrase = key.strip().encode()

@given('secret 32 bytes passphrase {key}')
def step_imp(context, key):
  context.passphrase = key.strip().encode()
  assert len(context.passphrase) == 32

@when('I encrypt the resulted content with the resulted passphrase using AES')
def step_imp(context):
  context.result = AES(context.passphrase).encrypt(context.content)

@when('I decrypt the content with the resulted passphrase using AES')
def step_imp(context):
  context.result = AES(context.passphrase).decrypt(context.content)

@when('I encode encrypted content with Base64')
def step_imp(context):
  pass

@when('I made PKCS7 padding of passphrase to 32 bytes')
def step_imp(context):
  pass

@when('I made PKCS7 padding of content to 16 bytes block size')
def step_imp(context):
  pass

@when('I made PKCS7 unpadding of decoded content for 16 bytes block size')
def step_imp(context):
  pass

@when('I decode encrypted content with Base64')
def step_imp(context):
  pass

@given('result shoud be {result}')
def step_imp(context, result):
  assert result.strip().encode() == context.result 